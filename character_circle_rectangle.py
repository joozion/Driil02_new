Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

whild True:
    run_circle()
    run_rectangle()

close_canvas()
