# find_blue_cup

This is a test project. The goal is to detect blue cup on the video and show series of images with printing bounded boxes with the cup.
The project consists of script for video frames processing (by using OpenCV) and for Flask server running.


## How to run
```bash

$ virtualenv env
$ source env/bin/activate
$ pip install requirements.txt
$ cd find_blue_cup
$ python3 app.py

```

After the first run script processes the video and creates image files in static folder.
