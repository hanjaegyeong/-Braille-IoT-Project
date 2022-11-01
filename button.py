import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
           
while True:
    value = GPIO.input(24)
    if value == True:
        time.sleep(1)
        import camera
        time.sleep(2)
        import ocr
        time.sleep(2)
        import mp3save
        time.sleep(4)
        import sound
        time.sleep(2)
        break
    time.sleep(0.1)