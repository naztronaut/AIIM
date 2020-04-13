import os
# import subprocess
import requests as requests

# Slack: CptHost.exe
# Teams: Teams.exe
# Teams window name is "Meeting | Microsoft Teams"
# Teams only works if the Meeting started on Teams AND you did not try to do something else in teams because the
# window title changes.
proc_list = ['CptHost.exe', 'Meeting | Microsoft Teams']

tasklist_query = ''

PI_URL = 'http://192.168.1.239'

for task in proc_list:
    tasklist_query += ''

#  Need the /v for verbose. /fi filters the process and looks for window title for Teams meeting
p = os.popen('tasklist /fo table /v /fi "imagename eq CptHost.exe" && '
             'tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*" /nh').read().splitlines()
# p = os.popen('tasklist /fo table /v').read().splitlines()
# p = subprocess.check_output(['tasklist'])

is_it_running = 0
for item in p:
    # Still needs condition because otherwise the console returns "No tasks are running for specific criteria"
    if item.find("CptHost.exe") > -1 or item.find("Teams.exe") > -1:
        is_it_running += 1
    #     print(item)
    # print(is_it_running)

if is_it_running > 0:
    requests.get(PI_URL + '/led/?status=on')
else:
    requests.get(PI_URL + '/led/?status=off')

