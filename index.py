from phue import Bridge
from time import sleep
from flask import Flask
# 100% = 254

bridge = Bridge('192.168.178.28')

ROOM = 'The room'

connected = bridge.connect()

state = bridge.get_api()

app = Flask(__name__)
LIGHTS = bridge.get_light_objects()


@app.route('/room-on')
def roomOn():
    bridge.set_group(ROOM, 'on', True)
    return 'on'


@app.route('/room-off')
def roomOff():
    bridge.set_group(ROOM, 'on', False)
    return 'off'


@app.route('/room-toggle')
def roomToggle():
    if(bridge.get_group(ROOM, 'on')):
        print('is on')
        bridge.set_group(ROOM, 'on', False)
    else:
        print('is off')
        bridge.set_group(ROOM, 'on', True)
    return 'toggle'


@app.route('/room-up')
def roomBrightnessUp():
    for light in LIGHTS:
        light.brightness += 25

    return 'brightness up'


@app.route('/room-down')
def roomBrightnessDown():
    for light in LIGHTS:
        light.brightness -= 25
    return 'brightness down'


@app.route('/room-scene/<sceneName>')
def roomScene(sceneName):
    bridge.run_scene(ROOM, sceneName)
    return 'Running scene: ' + sceneName


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9094)
