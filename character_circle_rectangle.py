Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')

    
    cx, cy, r = 400, 300, 200
    for deg in range(0, 360, 1):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)
    

def run_rectangle():
    print('RECTANGLE')

    for x in range(50, 750+1, 10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        delay(0.01)
    pass

while True:
    run_circle()
    run_rectangle()

close_canvas()
