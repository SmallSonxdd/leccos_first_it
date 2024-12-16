from graphics import Window
from button_actions import *
from T1_generation import *


def main():
    tokens_database = populate_T1_tokens(8,8)
    #tokens_database[1][tokens_database[0][0]][3] = 'Depleted'
    tokens_database[1][tokens_database[0][0]][2] = '51J65TMP'
    tokens_database[1][tokens_database[0][1]][2] = 'E8146KMT'
    #print(tokens_database)
    win = Window(800, 600)
    draw_buttons(win, tokens_database)
    win.wait_for_close()


main() 