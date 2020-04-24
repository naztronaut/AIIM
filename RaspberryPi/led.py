from flask import Flask, request, jsonify
import led_service as ls

app = Flask(__name__)


# {{url}}/led?type={{simple/neopixel}}&status=on/off
@app.route('/', methods=['GET'])
def led():
    led_type = request.args.get('type')
    status = request.args.get('status')
    if 'theme' in request.args:
        theme = request.args.get('theme')
    else:
        theme = 'random'
    resp = ls.update_led(led_type, status, theme)
    return jsonify({"message": resp})


# Currently only returns meeting status for 'neopixel' mode
# {{url}}/led/meeting_status
@app.route('/meeting_status', methods=['GET'])
def meeting_status():
    current_status = ls.get_neopixel_meeting_status()
    return jsonify({"meeting_status": current_status})
