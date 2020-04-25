import RPi.GPIO as GPIO
import os

# Uses GPIO Pin 18 by default - change this if you want to use another pin
PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)


def update_led(led_type, status, theme):
    if led_type == 'simple':
        if status == "on":
            GPIO.output(PIN, GPIO.HIGH)
            return "Led successfully turned on"
        elif status == "off":
            GPIO.output(PIN, GPIO.LOW)
            return "Led successfully turned off"
        else:
            return "Not a valid status"
    elif led_type == 'neopixel':
        # Get the status of neopixel_status.txt to determine whether or not to make the call to neopix.py
        with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'r') as f:
            is_it_currently_on = f.read().rstrip()
        if status == "on":
            if is_it_currently_on == '0':
                os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py on ' + theme)
            with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'w') as f:
                # Sets NeoPixel status as currently on
                f.write('1')
            return "NeoPixel successfully turned on"
        elif status == "off":
            if is_it_currently_on == '1':
                os.popen('sudo python3 ' + os.path.dirname(os.path.realpath(__file__)) + '/neopix.py off')
            with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'w') as f:
                # Sets NeoPixel status as currently off
                f.write('0')
            return "NeoPixel successfully turned off"
        else:
            return "Not a valid status"


# Currently only supports neopixel meeting status - returns true or false
def get_neopixel_meeting_status():
    with open(os.path.dirname(os.path.realpath(__file__)) + '/neopixel_status.txt', 'r') as f:
        is_it_currently_on = f.read().rstrip()
    if is_it_currently_on == '1':
        return True
    elif is_it_currently_on == '0':
        return False
