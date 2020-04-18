# Change this to your Pi's URL
PI_URL = 'http://192.168.1.239'
URL_CONTEXT = 'led'
# LED_TYPE should either be 'simple' or 'neopixel'
LED_TYPE = 'neopixel'
ZOOM = True
TEAMS = True
# To add flexibility later for multiple devices.
# USERNAME = 'naz'


# TODO Write this better
# Note: Need the /v for verbose. /fi filters the process and looks for window title for Teams meeting
def tasklist_query():
    if ZOOM is True and TEAMS is False:
        query = 'tasklist /fo table /v /fi "imagename eq CptHost.exe"'
    elif ZOOM is False and TEAMS is True:
        query = 'tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*"'
    else:
        query = 'tasklist /fo table /v /fi "imagename eq CptHost.exe" && ' \
                'tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*" /nh'

    return query
