from flask import Flask, render_template, Response
from camera import videocamera
from flask import Flask
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import Response
from flask import jsonify
import serial
import os
import pynmea2
from datetime import datetime
import time 
import numpy as np
import subprocess

import layoutmodule
import collections
import json
import requests

app = Flask(__name__)
app.secret_key = 'random string'
video_camera = None
global_frame = None
@app.route('/', methods = ['GET', 'POST'])
def login():
   """ 
   Documentation for login.   
   Creating username and password for login fucntion of web application.
   """
   error = None
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != '123':
         error = 'Invalid username or password. Please try again!'
      else:
         flash('You were successfully logged in')
         return redirect(url_for('layout'))			
   return render_template('login.html', error = error)
   
@app.route('/layout', methods = ['GET', 'POST']) 
def layout():
	"""
	Documentation for get Config data from VCJ server.
	"""
	return layoutmodule.layout_file()
	
@app.route('/layout/home', methods = ['GET', 'POST'])
def home():
	"""
	Documentation for home page.
	Creating home page of web application.
	"""
	return render_template('layout.html')
	
@app.route('/layout/camera')
def camera():
	localtime = time.localtime(time.time())
	datetime = str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])+" "+str(localtime[3])+":"+str(localtime[4])+":"+str(localtime[5])		
	
	video_dir = '/home/pi/Desktop/streaming/static'
	video_file_name = [f for f in os.listdir(video_dir) if f.endswith('.swf')]
	video_files_number = len(video_file_name)
	return render_template("camera.html",time=datetime,video_files_number = video_files_number,video_file_name = video_file_name)

@app.route('/camera', methods=['POST'])
def record_status():
    global video_camera 
    """
	Documentation for check status of video camera module.     
	"""
    if video_camera == None:
       video_camera = videoCamera()

    json = request.get_json()

    status = json['status']
	
    if status == "true":
        video_camera.start_record()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        return jsonify(result="stopped")
        
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/layout/camera/video_feed')
def video_feed():
    return Response(gen(videocamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
