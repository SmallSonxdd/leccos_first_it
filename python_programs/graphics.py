from tkinter import Tk, BOTH, Canvas, Scrollbar, Entry, Frame
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

class CustomFrame:
    def __init__(self, parent, pos_x, pos_y, width, height, scrollable=False):
        self.parent = parent
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.scrollable = scrollable
        
        self.frame = Frame(self.parent, width=self.width, height=self.height)
        self.frame.place(x=self.pos_x, y=self.pos_y)

        if self.scrollable:
            self.canvas = Canvas(self.frame, width=self.width, height=self.height)
            self.canvas.pack(side='left', fill='both', expand=True)
            self.inner_frame = Frame(self.canvas)
            self.canvas.create_window((0,0), window=self.inner_frame, anchor='nw')
            self.canvas.configure(scrollregion=(0, 0, self.width, self.height))
            self.inner_frame.bind("<Configure>", self.on_frame_configure)
        
        else:
            self.canvas = None
            self.inner_frame = self.frame
    
    def on_frame_configure(self, event):
        if self.scrollable:
            self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def add_widget(self, widget, **kwargs):
        widget.place(**kwargs)
        

    def destroy(self):
        self.frame.destroy()
        

class CustomButton:
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

    def delete(self):
        self.entry.delete(0, len(self.entry.get()))

class GridWidget:
    def __init__(self, canvas, pos_x, pos_y, cell_width, cell_height):
        self.canvas = canvas
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cell_width = cell_width
        self.cell_height = cell_height

        self.rows = 0
        self.cols = 0
        self.grid_items = []
    
    def add_single_item(self, item):
        self.grid_items.append(item)

    def add_multiple_items(self, list_of_items):
        self.grid_items.extend(list_of_items)

    def destroy(self):
        pass #maybe something

