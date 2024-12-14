from graphics import Window
from button_actions import *
from T1_generation import *


def main():
    tokens_database = populate_T1_tokens(8,8)
    win = Window(800, 600)
    draw_buttons(win, tokens_database)
    win.wait_for_close()


main() 