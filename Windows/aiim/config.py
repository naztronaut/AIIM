# Change this to your Pi's URL
PI_URL = 'http://192.168.1.239'
URL_CONTEXT = 'led'
# LED_TYPE should either be 'simple' or 'neopixel'
LED_TYPE = 'neopixel'
ZOOM = True
TEAMS = True
SLACK = True
THEME = 'random'  # valentines, cool, nature, random (blank = random)
# To add flexibility later for multiple devices.
# USERNAME = 'naz'


# Note: Need the /v for verbose. /fi filters the process and looks for window title for Teams meeting
def tasklist_query():
    # Initialize the query so the rest can be appended
    query = 'echo "============= Starting tasklist ============="'
    if ZOOM is True:
        query += ' && tasklist /fo table /v /fi "imagename eq CptHost.exe"'
    if TEAMS is True:
        query += '&& tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*"'
    if SLACK is True:
        query += '&& tasklist /fo table /v /fi "imagename eq Slack.exe" /fi "windowtitle eq call*"'
    return query
