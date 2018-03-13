from flask import Flask, render_template
import os, pickle

labels = pickle.load(open('./static/rects.p', 'rb'))


app = Flask(__name__)
app.debug = True

import index

app.run()