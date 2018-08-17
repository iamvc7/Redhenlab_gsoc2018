
from pathlib import Path
from shutil import copyfile
import os
from distutils.dir_util import copy_tree

p1 = '/home/paperspace/Cooking_Activity/newformat/t_video/' 
p2 = '/home/paperspace/Cooking_Activity/newformat/t_json/'
dest = '/home/paperspace/Cooking_Activity/newformat/op_format/'

p = Path(p1)
for path in p.glob('*.avi'):
    video_path = str(path)
    video = video_path.split('/')[-1]
    os.chdir(p2)
    p3 = os.getcwd()
    p4 = os.path.join(p3,video)
    copy_tree(p4,dest)
