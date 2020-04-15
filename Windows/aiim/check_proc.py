import os
# import subprocess
import requests as requests
import config


def find_processes():
    #  Need the /v for verbose. /fi filters the process and looks for window title for Teams meeting
    p = os.popen(config.tasklist_query()).read().splitlines()
    print(config.tasklist_query())
    is_it_running = 0
    for item in p:
        # Still needs condition because otherwise the console returns "No tasks are running for specific criteria"
        if item.find("CptHost.exe") > -1 or item.find("Teams.exe") > -1:
            is_it_running += 1

    change_led_status(is_it_running)


def change_led_status(is_it_running):
    if is_it_running > 0:
        requests.get(config.PI_URL + '/led/?status=on')
    else:
        requests.get(config.PI_URL + '/led/?status=off')

# p = subprocess.check_output(['tasklist'])


find_processes()
