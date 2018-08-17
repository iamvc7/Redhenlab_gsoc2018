
import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import csv
from collections import OrderedDict
import pickle
import json
import os
from os import path
import re

def findfiles(path, filename):
    #regObj = re.compile(regex)
    res = []
    for root, dirs, fnames in os.walk(path):
        for fname in fnames:
            if filename == fname.split('.')[0]:
                res.append(os.path.join(root, fname))
    return res
     

with open('sorted_video_reordered.csv') as f:   
    read = csv.reader(f, delimiter=',')
    next(read)
    b = {}
    a = []
    path = '/home/paperspace/Cooking_Activity/resized_videos/' 
    p2 = '/home/paperspace/Cooking_Activity/trimmed_videos_classwise'
    #a.append(['filename','label_index','label','st_frame','end_frame'])
    for row in read:
        #print(row[3],row[4])
        filename = row[0]
        st_frame = row[3]
        end_frame = row[4]
        st_time = int(st_frame)/(30)
        end_time = int(end_frame)/(30)
        #print(st_time,end_time)
        label_index = row[1]
        res = findfiles(path,filename)
        print (res)
        saving_path = os.path.join(p2,str(filename)+str('_i')+str('__')+str(label_index)+str('.avi'))
        while os.path.exists(saving_path):
            t = saving_path.split('__')
            t[0] = t[0] + str('i')
            saving_path = '__'.join(t)
        ffmpeg_extract_subclip(res[0], st_time, end_time, targetname=saving_path)
       
            
