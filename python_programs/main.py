import os
from graphics import Window
from button_actions import *


def main():
    win = Window(800, 600)
    draw_buttons(win)
    win.wait_for_close()


main() 