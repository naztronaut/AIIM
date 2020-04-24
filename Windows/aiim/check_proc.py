import os
import requests as requests
import config


def find_processes():
    p = os.popen(config.tasklist_query()).read().splitlines()
    is_it_running = 0
    for item in p:
        # Still needs condition because otherwise the console returns "No tasks are running for specific criteria"
        if config.ZOOM is True and item.find('CptHost.exe') > -1:
                is_it_running += 1
        if config.TEAMS is True and item.find('Teams.exe') > -1:
                is_it_running += 1
    change_led_status(is_it_running)


# Shouldn't need to change anything below - if you need to change the URL, context, or led type, check config.py
def change_led_status(is_it_running):
    if is_it_running > 0:
        requests.get("%s/%s?type=%s&theme=%s&status=on" % (config.PI_URL, config.URL_CONTEXT, config.LED_TYPE, config.THEME))
    else:
        requests.get("%s/%s?type=%s&status=off" % (config.PI_URL, config.URL_CONTEXT, config.LED_TYPE))


find_processes()
