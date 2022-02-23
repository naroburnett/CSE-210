from mimetypes import init
from pyray import *
init_window(800, 450, "hello")
while not window_should_close():
    begin_drawing()
    clear_background(WHITE)
    draw_text('hello world', 190, 200, 20, VIOLET_1)
    end_drawing()
close_window()