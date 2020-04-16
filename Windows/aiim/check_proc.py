import os
# import subprocess
import requests as requests
import config


def find_processes():
    #  Need the /v for verbose. /fi filters the process and looks for window title for Teams meeting
    p = os.popen(config.tasklist_query()).read().splitlines()
    is_it_running = 0
    for item in p:
        print(item)
        # Still needs condition because otherwise the console returns "No tasks are running for specific criteria"
        if config.ZOOM is True and item.find('CptHost.exe') > -1:
                is_it_running += 1
        if config.TEAMS is True and item.find('Teams.exe') > -1:
                is_it_running += 1

    change_led_status(is_it_running)


def change_led_status(is_it_running):
    if is_it_running > 0:
        requests.get("%s/%s?status=on" % (config.PI_URL, config.URL_CONTEXT))
    else:
        requests.get("%s/%s?status=off" % (config.PI_URL, config.URL_CONTEXT))


find_processes()
