
import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
parser = argparse.ArgumentParser(description='Process some videos')
parser.add_argument("--video")
parser.add_argument("--res")
args = vars(parser.parse_args())

ffmpeg_extract_subclip(args["video"], 0, 59, targetname=args["res"])
