import os
import moviepy.editor as mp
from datetime import datetime

# loop through all mp4 files in the same directory
for filename in os.listdir():
    if filename.endswith(".mp4"):
        clip = mp.VideoFileClip(filename)
        clip = clip.crop(x1=0, y1=150, x2=0, y2=clip.h - 150) #crop top and bottom 150px
        clip = clip.subclip(0, -3) #remove last 3 secs
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S") #get timestamp
        new_filename = timestamp + ".mp4" #use timestamp as filename
        clip.write_videofile(new_filename) #write the new video
