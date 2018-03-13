from flask import render_template
from app import labels, app

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
