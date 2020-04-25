import sys
import board
import neopixel
import random
import themes

# Change to the number of LEDs you are using
LED_COUNT = 142
# Uses GPIO Pin 18. if you want to use another pin, change the D18 to some other pin
pixels = neopixel.NeoPixel(board.D18, LED_COUNT)

try:
    led_status = sys.argv[1]
except:
    print("Missing LED_STATUS argument")
    sys.exit()

try:
    theme = sys.argv[2]
except:
    theme = 'random'


def theme_colors():
    if theme == 'random':
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    else:
        chosen_theme = themes.pick_theme(theme)
        size = len(chosen_theme)
        color = chosen_theme[random.randint(0, size-1)]
        return color[0], color[1], color[2]


if led_status == 'on':
    for x in range(0, LED_COUNT):
        pixels[x] = (theme_colors())
elif led_status == "off":
    for x in range(0, LED_COUNT):
        pixels[x] = (0, 0, 0)
else:
    print("Unknown state")
