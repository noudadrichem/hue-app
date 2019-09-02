import RPi.GPIO as GPIO
from time import sleep
import urllib.request

API_URL = 'http://192.168.178.32:9094'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:  # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        sleep(10)
        f = urllib.request.urlopen("http://stackoverflow.com")
        print(f.read())
