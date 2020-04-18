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
        if status == "on":
            os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py on')
            return jsonify({"message": "NeoPixel successfully turned on"})
        elif status == "off":
            os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py off')
            return jsonify({"message": "NeoPixel successfully turned off"})
        else:
            return jsonify({"message": "Not a valid status"})
