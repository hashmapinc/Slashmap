from picamera import PiCamera

import settings

camera = PiCamera()

def takePicture():
    camera.capture(settings.IMG_PATH)