from signal import pause
from datetime import datetime

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from gpiozero import Button

button1 = Button(17)
button2 = Button(27)


picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
moment = datetime.now()

encoder = H264Encoder(10000000)
output = FfmpegOutput('video2_%02d_%02d_%02d.mp4' % (moment.hour, moment.minute, moment.second), audio=False)

def recording():
    print("ready")
    picam2.start_recording(encoder, output)

def stop_recording():
    print("done")
    picam2.stop_recording()

button1.when_pressed = recording
button2.when_pressed = stop_recording

pause()
