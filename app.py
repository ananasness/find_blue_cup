from flask import Flask
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

import index

app.run()