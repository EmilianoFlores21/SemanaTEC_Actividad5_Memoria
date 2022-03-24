from random import *
from turtle import *
from freegames import path

car = path('car.gif')
"Color codes for tiles"
tiles = ["#000000","#333333","#878787","#ffffff",
"#ffb5b5","#ff6363","#ff0000","#800000",
"#400000","#451f11","#bf00ff","#b3755f",
"#ff8b61","#e35c2b","#ff4400","#ff9100",
"#7d4b09","#ffd000","#a2ff00","#496b0f",
"#819c52","#29731a","#144a09","#03bf00",
"#04ff00","#06c96b","#0b8059","#0b7c80",
"#00f7ff","#0077ff","#0008ff","#5900ff",] * 2
state = {'mark': None}
hide = [True] * 64

tap_counter = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    global tap_counter
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        tap_counter = tap_counter + 1
        print("Taps Count: ",tap_counter)
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()

        goto(x, y)
        down()
        color('black', tiles[mark])
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()