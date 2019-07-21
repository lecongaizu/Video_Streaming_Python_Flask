import cv2
import threading
from datetime import datetime
import time
import subprocess
import os
import os, sys
from subprocess import call
import json 
import collections 
import os, fnmatch
import sqlite3 as sql
from datetime import timedelta
class videocamera(object):
    def __init__(self):
        # using opencv to capture from device 0. if you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.      
        self.video = cv2.VideoCapture(0)
        # if you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.videocapture('video.mp4')
    
    def __del__(self):
        self.video.release()
        
    def start_record(file):
        cmd = "ffmpeg -f video4linux2 -s 1080x720 -i /dev/video0 -thread_queue_size 16384 -f alsa -ac 2 -i hw:1,0 -acodec libmp3lame -ab 128k -ar 44100 -async 1 -f segment -strftime 1 -segment_time 20 -reset_timestamps 1 -segment_format swf /home/pi/desktop/streaming/static/%y-%m-%d_%h-%m-%s.swf"
        subprocess.call(cmd, shell=true)
    
    def stop_record(self):
        self.is_record = False
        cmd = "sudo killall ffmpeg"	
        subprocess.call(cmd,shell= True)
		
    def get_frame(self):
        success, image = self.video.read()
        # we are using motion jpeg, but opencv defaults to capture raw images,
        # so we must encode it into jpeg in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

	
