from tkinter import Tk, BOTH, Canvas
import time
import random


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Leccos')
        self.canvas = Canvas(self.__root, bg='blue', height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol('WM_DELETE_WINDOW', self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()
        print('Window successfully closed!')
    
    def close(self):
        self.running = False

class Button:
    def __init__(self, win, type_of_button, link, pos_x, pos_y, size):
        self.win = win
        self.type_of_button = type_of_button
        self.link = link
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width, self.height = size
        self.button_id = None
        self.text_id = None

    def draw(self):
        self.button_id = self.win.canvas.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.width, self.pos_y + self.height, fill='lightblue', outline='black')
        self.text_id = self.win.canvas.create_text(self.pos_x + self.width/2, self.pos_y + self.height/2, text = self.type_of_button, fill='black')

    def bind_click(self, action):
        def on_click(event):
            if (self.pos_x <= event.x <= self.pos_x + self.width and self.pos_y <= event.y <= self.pos_y + self.height):
                action()
        self.win.canvas.tag_bind(self.button_id, "<Button-1>", on_click)
        self.win.canvas.tag_bind(self.text_id, "<Button-1>", on_click)




