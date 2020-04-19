from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import os

# Uses GPIO Pin 18 by default - change this if you want to use another pin
PIN = 18

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)


# {{url}}/led?type={{simple/neopixel}}&status=on/off
@app.route('/', methods=['GET'])
def led():
    led_type = request.args.get('type')
    if led_type == 'simple':
        status = request.args.get('status')
        if status == "on":
            GPIO.output(PIN, GPIO.HIGH)
            return jsonify({"message": "Led successfully turned on"})
        elif status == "off":
            GPIO.output(PIN, GPIO.LOW)
            return jsonify({"message": "Led successfully turned off"})
        else:
            return jsonify({"message": "Not a valid status"})
    elif led_type == 'neopixel':
        status = request.args.get('status')
        # Get the status of neopixel_status.txt to determine whether or not to make the call to neopix.py
        with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'r') as f:
            is_it_currently_on = f.read().rstrip()
        if status == "on":
            if is_it_currently_on == '0':
                os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py on')
            with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'w') as f:
                # Sets NeoPixel status as currently on
                f.write('1')
            return jsonify({"message": "NeoPixel successfully turned on"})
        elif status == "off":
            if is_it_currently_on == '1':
                os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py off')
            with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'w') as f:
                # Sets NeoPixel status as currently off
                f.write('0')
            return jsonify({"message": "NeoPixel successfully turned off"})
        else:
            return jsonify({"message": "Not a valid status"})


# Currently only returns meeting status for 'neopixel' mode
@app.route('/meeting_status', methods=['GET'])
def meeting_status():
    with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'r') as f:
        is_it_currently_on = f.read().rstrip()

    if is_it_currently_on == '1':
        return jsonify({"meeting_status": True})
    elif is_it_currently_on == '0':
        return jsonify({"meeting_status": False})
