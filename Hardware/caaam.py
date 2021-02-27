from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
# for i in range(5):
#     sleep(5)
#     camera.capture('/home/pi/Desktop/image%s.jpg' % i)


# for mode in camera.EXPOSURE_MODES:
#     camera.exposure_mode = mode
#     camera.annotate_text = "Mode: %s" % mode
#     sleep(5)
#     camera.capture('/home/pi/Desktop/image%s.jpg' % mode)

sleep(25)
camera.stop_preview()
print('hello')

