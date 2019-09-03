import RPi.GPIO as GPIO
from time import sleep
import requests

API_URL = 'http://192.168.178.39:9094'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pinsEndpoints = [
        {
            'pin': 10,
            'endpoint': '/room-toggle'
        },     
        {
            'pin': 8,
            'endpoint': '/room-scene/Vibing'
        }
]

def togglePin(pinNum, endpoint):
    input_state = GPIO.input(pinNum)
    if input_state == False:
        response = requests.get(API_URL + endpoint)
        print('btn pressed', response.text)

while True:
    for i in range(len(pinsEndpoints)):
        togglePin(pinsEndpoints[i]['pin'], pinsEndpoints[i]['endpoint'])
    sleep(0.2)



