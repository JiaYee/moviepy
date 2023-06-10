import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime

# Iterate through files in current directory
for filename in os.listdir('.'):
    if filename.endswith('.mp4'):
        # Get current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Load video file clip
        video = VideoFileClip(filename)

        # Cut first 59 seconds
        short_video = video.subclip(0, 59)

        # Define output filename based on timestamp
        output_filename = timestamp + '_shorts.mp4'

        # Save short video to file
        short_video.write_videofile(output_filename)

        # Close video file clip
        video.close()
