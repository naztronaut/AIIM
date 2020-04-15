# Change this to your Pi's URL
PI_URL = 'http://192.168.1.239'
ZOOM = True
TEAMS = True


# TODO Write this better
def tasklist_query():
    if ZOOM is True and TEAMS is False:
        query = 'tasklist /fo table /v /fi "imagename eq CptHost.exe"'
    elif ZOOM is False and TEAMS is True:
        query = 'tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*"'
    else:
        query = 'tasklist /fo table /v /fi "imagename eq CptHost.exe" && ' \
                'tasklist /fo table /v /fi "imagename eq Teams.exe" /fi "windowtitle eq Meet*" /nh'

    return query
