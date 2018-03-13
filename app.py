from flask import Flask, render_template
import os, pickle
from pathlib import Path
from script import process_video

label_file = Path("./static/rects.p")
labels = None

if not label_file.is_file():
    try:
        os.mkdir("./static")
        os.mkdir("./static/res")

    except FileExistsError:
        pass

    video_file = Path("./static/video.mp4")
    if not video_file.is_file():
        print('Please put file named as "video.mp4" into static folder to ')
        exit(1)

    else:
        process_video('./static/video.mp4')


labels = pickle.load(open('./static/rects.p', 'rb'))


app = Flask(__name__)
app.debug = True

filename = '/static/res/{}.jpg'

@app.route("/")
def hello():
    pictures = []
    for i in range(1, len(labels)):
        if ((labels[i - 1] == 'no cup here' and labels[i] != 'no cup here') or
                (labels[i - 1] != 'no cup here' and labels[i] == 'no cup here')):
            pictures.append((filename.format(i-1), labels[i-1], i-1))
            pictures.append((filename.format(i), labels[i], i))

    return render_template('index.html', pictures=pictures)


@app.route("/all")
def show_all():
    pictures = [(filename.format(i), labels[i], i) for i in range(len(labels))]
    return render_template('index.html', pictures=pictures)


app.run()