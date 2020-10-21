WIDTH = 500
HEIGHT = 500

x = 10
y = 10
a = 5
b = 2
beep = tone.create('A5', 0.5)
boop = tone.create('A3', 0.5)

def draw():
    screen.clear()
    screen.blit('alien', (x, y))

def update():
    global x, y, a, b
    x += a
    y += b
    if x >= 430 or x <= 10:
        a *= -1
        beep.play()

    if y >= 400 or y <= 10:
        b *= -1
        boop.play()

def on_mouse_down(pos):
    global b
    b *= -1