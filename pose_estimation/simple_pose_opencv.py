import cv2
import numpy as np
import time
import glob
import os

def pose_estimation(input_image):
    img = cv2.imread(input_image)
    protoFile = "./models/pose_deploy_linevec.prototxt"
    weightFile = "./models/pose_iter_440000.caffemodel"
    nPoints = 18
    POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]
    input_width = 368
    input_height = 368
    threshold = 0.1

    img_height = img.shape[0]
    img_width = img.shape[1]

    input_blob = cv2.dnn.blobFromImage(img, 1.0/255, (input_width, input_height), (0,0,0), swapRB=False, crop=False)
    net = cv2.dnn.readNetFromCaffe(protoFile, weightFile)
    net.setInput(input_blob)
    output = net.forward()
    H = output.shape[2]
    W = output.shape[3]
    points = []
    for i in range(nPoints):
        probMap = output[0,i,:,:]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        x = (img_width * point[0]) / W
        y = (img_height * point[1]) / H
        if prob > threshold:
            #cv2.circle(img, (int(x), int(y)), 15, (0,255,255), thickness=-1, lineType=cv2.FILLED)
            points.append((int(x),int(y)))
        else:
            points.append(None)

    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
        if points[partA] and points[partB]:
            cv2.line(img, points[partA], points[partB], (0,255,255),1,lineType=cv2.LINE_AA)
            cv2.circle(img, points[partA], 4, (150,0,0), thickness=-5, lineType=cv2.FILLED)
            cv2.circle(img, points[partB], 4, (150,0,0), thickness=-5, lineType=cv2.FILLED)

    return img


def main():
    files = glob.glob("Input/*.jpg")
    for file in files:
        tic = time.time()
        output = pose_estimation(file)
        out = file.split('/')[1]
        dirname = "Output"
        #cv2.imwrite('result.jpg',img)
        cv2.imwrite(os.path.join(dirname, out), output)
        toc = time.time()
        print ('processing time is %.5f' % (toc - tic))

main()
