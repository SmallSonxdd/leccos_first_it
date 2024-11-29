from tkinter import Tk, BOTH, Canvas, Scrollbar, Entry
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
        self.widgets = {}
    
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


class CustomScrollbar:
    def __init__(self, canvas, orientation, pos_x, pos_y, size_x, size_y):
        self.canvas = canvas
        self.orientation = orientation
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y


    def draw(self):
        self.scrollbar = Scrollbar(self.canvas, orient=self.orientation)
        self.scrollbar.place(x=self.pos_x, y=self.pos_y, width=self.size_x, height=self.size_y)
    
    def set_command(self, command):
        self.scrollbar.config(command=command)
    
    def get_scrollbar(self):
        return self.scrollbar
    
    def destroy(self):
        self.scrollbar.destroy()

class CustomEntry:
    def __init__(self, canvas, pos_x, pos_y, size_x, size_y):
        self.entry = Entry(canvas)
        self.entry.place(x=pos_x, y=pos_y, width=size_x, height=size_y)

    def destroy(self):
        self.entry.destroy()