from signal import pause
from datetime import datetime

from picamera2 import Picamera2
from gpiozero import Button

button1 = Button(17)

picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration())
picam2.start()

def take_picture():
    moment = datetime.now()
    filename = 'image_%02d_%02d_%02d.jpg' % (
        moment.hour, moment.minute, moment.second
    )
    print("Taking picture...")
    picam2.capture_file(filename)
    print("Picture saved:", filename)

button1.when_pressed = take_picture

print("Ready to take pictures. Press the button.")
pause()
