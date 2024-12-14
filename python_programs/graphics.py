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
        
        self.width = canvas.winfo_width()
        self.height = canvas.winfo_height()

        self.rows = 0
        self.cols = 3
        self.grid_items = []
    
    def add_single_item(self, item):
        self.grid_items.append(item)

    def add_multiple_items(self, list_of_items):
        self.grid_items.extend(list_of_items)

    # Forward create_rectangle to the internal canvas
    def create_rectangle(self, *args, **kwargs):
        return self.canvas.create_rectangle(*args, **kwargs)

    # Forward create_text to the internal canvas
    def create_text(self, *args, **kwargs):
        return self.canvas.create_text(*args, **kwargs)

    # Forward tag_bind to the internal canvas
    def tag_bind(self, tag, event, callback):
        self.canvas.tag_bind(tag, event, callback)

    def draw(self):        
        length = len(self.grid_items)
        self.rows = (length + self.cols - 1) // self.cols
        for index, item in enumerate(self.grid_items):
            row = index // self.cols  # Calculate row number
            col = index % self.cols  # Calculate column number

            x = self.pos_x + col * self.cell_width
            y = self.pos_y + row * self.cell_height

            item.draw(x, y)
    def itemconfig(self, item_id, **kwargs):
        """
        Update the properties of an item on the canvas.
        :param item_id: The ID of the canvas item to configure.
        :param kwargs: Key-value pairs of properties to update.
        """
        self.canvas.itemconfig(item_id, **kwargs)    
    
    def update_dimensions(self):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
    
    
class TokenWidget:
    #grid is object of GridWidget class and token is an entry in dictionary of culture/open_world -> 
    # tuple(list of attributes, token code, status, random values)
    def __init__(self, grid, size, token): 
        self.grid = grid
        self.size = size
        self.token = token

        self.square_id = None
        self.name_id = None
        self.status_id = None
        self.code_id = None
        self.tooltip_id = None
        self.text_id = None

    def draw(self, x, y):
        self.square_id = self.grid.create_rectangle(x, y, x + self.size, y + self.size, fill='lightgrey', outline='black')

        self.grid.tag_bind(self.square_id, "<Enter>", self.on_hover)
        self.grid.tag_bind(self.square_id, "<Leave>", self.on_hover_exit)

        name_text = self.token.key
        self.name_id = self.grid.create_rectangle(x, y + self.size, x + self.size, y + self.size + 20, fill='lightblue', outline='black')
        self.grid.create_text(x + self.size/2, y + self.size + 10, text=f'Name: {name_text}', fill='black')
        if self.token.status == 'unused':
            status_color = 'green'
            status_text = 'Activate'
        elif self.token.status == 'used':
            status_color = 'red'
            status_text = 'Deactivated'
        else:
            raise Exception('Invalid token status')
        self.status_id = self.grid.create_rectangle(x, y + self.size + 20, x + self.size, y + self.size + 40, fill='lightblue', outline='black')
        self.grid.create_text(x + self.size/2, y + self.size + 30, text=f'Status: {status_text}', fill=status_color)
        self.code_id = self.grid.create_rectangle(x, y + self.size + 40, x + self.size, y + self.size + 60, fill='lightblue', outline='black')
        self.grid.create_text(x + self.size/2, y + self.size + 50, text=f'Code: {self.token.code}', fill='black')
    
    def on_hover(self, event):
        self.grid.itemconfig(self.square_id, fill="yellow")
    
    def on_hover_exit(self, event):
        self.grid.itemconfig(self.square_id, fill="lightgrey")


class Token:
    def __init__(self, key, token_population):
        self.key = key
        self.attributes = token_population[1][key][0]
        self.type = token_population[1][key][1]
        self.code = token_population[1][key][2]
        self.status = token_population[1][key][3]
        self.random_values = token_population[1][key][4]

    def __del__(self):
        print(f"Token {self.key} is being deleted!")

    #who knows whether I will use this
    def deactivate(self, token_population): #this is meant for when new token is created, it should 'deactivate' the tokens used for its creation
        token_population[self.key][3] = 'used'
        self.status = 'used'