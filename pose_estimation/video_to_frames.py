import cv2
import glob
import os

def video_frames():
    files = glob.glob("All-Scenes/*.mp4")
    for file in files:
        vidcap = cv2.VideoCapture(file)
        l = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(vidcap.get(cv2.CAP_PROP_FPS))
        dirname = file.split('/')[1]
        os.mkdir(dirname)
        success,image = vidcap.read()
        count = 0
        success = True
        for i in range(0,l,3):
            cv2.imwrite(os.path.join(dirname, "frame%d.jpg" % count), image)
            success,image = vidcap.read()
            count += 1
        print('Read a new Video: ', success)
