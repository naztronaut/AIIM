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
    elif theme == 'sunset':
        sunset_size = len(themes.sunset)
        # return random.randint(0, 255), random.randint(0, 128), random.randint(0, 36)
        chosen_color = themes.sunset[random.randint(0, sunset_size)-1]
        return chosen_color[0], chosen_color[1], chosen_color[2]
    elif theme == 'cool':
        cool_size = len(themes.cool)
        chosen_color = themes.cool[random.randint(0, cool_size)-1]
        return chosen_color[0], chosen_color[1], chosen_color[2]
    elif theme == 'nature':
        nature_size = len(themes.nature)
        chosen_color = themes.nature[random.randint(0, nature_size)-1]
        return chosen_color[0], chosen_color[1], chosen_color[2]
    else:
        print("Uknown theme. Choose from sunset, cool, and nature only")


if led_status == 'on':
    for x in range(0, LED_COUNT):
        pixels[x] = (theme_colors())
elif led_status == "off":
    for x in range(0, LED_COUNT):
        pixels[x] = (0, 0, 0)
else:
    print("Unknown state")
