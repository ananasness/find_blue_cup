from flask import Flask, render_template
import os, pickle
app = Flask(__name__)
app.debug = True


filename = '/static/res/{}.jpg'

@app.route("/")
def hello():
    labels = pickle.load(open('./static/rects.p', 'rb'))


    pictures = []
    for i in range(1, len(labels)):
        if ((labels[i - 1] == 'no cup here' and labels[i] != 'no cup here')
            or (labels[i - 1] != 'no cup here' and labels[i] == 'no cup here')):
            pictures.append((filename.format(i-1), labels[i-1], i-1))
            pictures.append((filename.format(i), labels[i], i))




    return render_template('index.html', pictures=pictures)

app.run()