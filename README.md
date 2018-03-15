# find_blue_cup

This is a test project. The goal is to detect blue cup on the video and show series of images with printing bounded boxes with the cup.
The project consists of script for video frames processing (using OpenCV) and for Flask server running.


## How to run
```bash

$ git clone https://github.com/ananasness/find_blue_cup
$ cd find_blue_cup
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python app.py

```

After the first run the program processes the video and creates image files in static folder.

Index page shows pairs of frames where the cup appears or disappears. Also page `/all` demonstrates all processed frames.
