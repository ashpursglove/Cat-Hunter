#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from catpack.camera_pi import Camera
from catpack import stepper, servo


app = Flask(__name__)




@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# STEPPER CONTROL
@app.route("/<deviceName>/<action>") 
def action(deviceName, action):
    
    
    servo.x.detach()

    
    actuator = '_'

    if deviceName == 'right':
        actuator = 'right'
    if deviceName == 'left':
        actuator = 'left'
        
    if action == "on" and actuator == 'right':
        stepper.forward()
        stepper.off()
        actuator = '_'
    elif action == "on" and actuator == 'left':
        stepper.backward()
        stepper.off()
        actuator = '_'
    else:
        stepper.off()
        actuator = '_'
        
    if deviceName == 'twitch' and action == 'on':
        servo.twitch()
        
        
        
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
#     app.run(debug=True, host='109.171.137.234', threaded=True)
