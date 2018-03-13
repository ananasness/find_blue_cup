import cv2 as cv
import pickle
import numpy as np

video_path = 'video.mp4'


def create_bound_method(frame):
    color_template = cv.cvtColor(frame, cv.COLOR_BGR2HSV)[210:370, 780:1000]

    means = color_template.mean(axis=(0, 1))
    stds = color_template.std(axis=(0, 1))
    coefs = np.array([13, 5, 2])
    color_bounds = np.array([means - stds * coefs, means + stds * coefs]).T

    def bound_method(imm, bounds=color_bounds):
        mask = [0, 0, 0]
        for i in range(3):
            mask[i] = cv.inRange(imm[:, :, i], *bounds[i, :, None])

        gmask = np.logical_and(mask[0] == 255, mask[1] == 255, mask[2] == 255)
        bounded_im = np.zeros(imm.shape[:2])
        bounded_im[gmask] = 255
        return bounded_im

    return bound_method


def find_rect(hsv_image, bound):
    im_hsv = hsv_image.copy()
    bounded = np.array(bound(im_hsv), dtype=np.uint8)
    bounded = cv.GaussianBlur(bounded, (9, 9), 5)
    kernel = np.ones((16, 16))
    bounded = cv.morphologyEx(bounded, cv.MORPH_ERODE, kernel)
    im2, contours, hierarchy = cv.findContours(bounded, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None
    lens = [len(contours[i]) for i in range(len(contours))]
    ind = np.argmax(lens)

    if lens[ind] < 100:
        return None
    brs = tuple(contours[ind].min(axis=0)[0]), tuple(contours[ind].max(axis=0)[0])

    return brs


def process_video(video_path):

    cap = cv.VideoCapture(video_path)
    frames = []
    i = 0
    while cap.isOpened() and i < 1000:
        i += 1
        print('\rloaded: {}'.format(i + 1), end='')

        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)

    cap.release()
    print()
    bound = create_bound_method(frames[51])
    rects = ['no cup here' for _ in range(len(frames))]

    for i in range(len(frames)):
        print('\rprocessed: {}/{}'.format(i + 1, len(frames)), end='')
        im = frames[i].copy()
        rect = find_rect(cv.cvtColor(im, cv.COLOR_BGR2HSV), bound)
        if rect != None:
            cv.rectangle(im, *rect, (255, 255, 0), 3)
            rects[i] = rect

        cv.imwrite('static/res/{}.jpg'.format(i), im)

    print()
    pickle.dump(rects, open('./static/rects.p', 'wb'))