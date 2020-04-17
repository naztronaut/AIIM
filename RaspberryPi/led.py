from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import board
import neopixel
import random

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

LED_COUNT = 142

pixels = neopixel.NeoPixel(board.D18, LED_COUNT)


# {{url}}/led?type={{simple/neopixel}}&status=on/off
@app.route('/', methods=['GET'])
def led():
    led_type = request.args.get('type')
    if led_type == 'simple':
        status = request.args.get('status')
        if status == "on":
            GPIO.output(18, GPIO.HIGH)
            return jsonify({"message": "Led successfully turned on"})
        elif status == "off":
            GPIO.output(18, GPIO.LOW)
            return jsonify({"message": "Led successfully turned off"})
        else:
            return jsonify({"message": "Not a valid status"})
    elif led_type == 'neopixel':
        status = request.args.get('status')
        if status == "on":
            for x in range(0, LED_COUNT):
                pixels[x] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            return jsonify({"message": "NeoPixel successfully turned on"})
        elif status == "off":
            for x in range(0, LED_COUNT):
                pixels[x] = (0, 0, 0)
            return jsonify({"message": "NeoPixel successfully turned off"})
        else:
            return jsonify({"message": "Not a valid status"})
