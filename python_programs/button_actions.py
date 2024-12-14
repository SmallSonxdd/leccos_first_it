import subprocess
import gc
from graphics import *

def draw_buttons(win, tokens_database):
    invitations = CustomButton(win, 'Invitations', "https://objkt.com/collections/KT1MFqZPJFhg5rUcW1VFxKrEKASMfsVg8Ukc",
    200, 250, (100, 50))
    invitations.draw()
    invitations.bind_click(lambda: open_webpage())
    forge = CustomButton(win, 'Forge', 'Forge process', 500, 250, (100, 50))
    forge.draw()
    forge.bind_click(lambda: redraw_forge(win, tokens_database))
    collection = CustomButton(win, 'Collection', 'Open collection', 700, 550, (85, 35))
    collection.draw()
    collection.bind_click(lambda: redraw_collection(win, tokens_database))
    settings = CustomButton(win, 'Settings', 'Open settings', 5, 545, (50, 50))
    settings.draw()
    #settings.bind_click(redraw_settings)
    pass


def open_webpage():
    subprocess.Popen(["brave-browser", "--password-store=basic", 
                      "https://objkt.com/collections/KT1MFqZPJFhg5rUcW1VFxKrEKASMfsVg8Ukc"])

def redraw_forge(win, tokens_database):
    win.canvas.delete('all')
    token_one = CustomButton(win, 'First token', 'Some link', 200, 250, (100, 50))
    token_one.draw()
    token_two = CustomButton(win, 'Second token', 'Some link', 500, 250, (100, 50))
    token_two.draw()
    accept_forge = CustomButton(win, 'Forge!', 'Some link', 350, 400, (100, 50))
    accept_forge.draw()
    back_button = CustomButton(win, 'Go back', 'Some link', 700, 550, (85, 35))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_main_page(win, tokens_database))
    pass

def redraw_collection(win, tokens_database):
    win.canvas.delete('all')
    list_of_token_instances = list_my_token_instances([], tokens_database)

    #Frame for grid
    frame_grid = CustomFrame(win.canvas, 15, 60, 678, 423, True)
    win.widgets['frame_grid'] = frame_grid
    
    #Grid for token widgets
    my_grid = GridWidget(frame_grid.canvas, 0, 0, 226, 300)
    list_of_token_widget_instances = list_my_token_widget_instances([], list_of_token_instances, my_grid)
    my_grid.add_multiple_items(list_of_token_widget_instances)
    my_grid.draw()

    #Scrollbar
    scrollbar = CustomScrollbar(win.canvas, "vertical", 700, 15, 85, 470)
    scrollbar.draw()
    scrollbar.set_command(frame_grid.canvas.yview)
    frame_grid.canvas.config(yscrollcommand=scrollbar.get_scrollbar().set)
    win.widgets['scrollbar'] = scrollbar

    #Search bar
    search_entry = CustomEntry(win.canvas, 15, 15, 630, 30)
    win.widgets['search_entry'] = search_entry

    #Clear button
    clear_button = CustomButton(win, 'Clear', 'Some link', 645, 15, (50, 30))
    clear_button.draw()
    clear_button.bind_click(lambda: search_entry.delete())

    #Back button
    back_button = CustomButton(win, 'Go back', 'Some link', 700, 500, (85, 85))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_main_page(win, tokens_database, list_of_token_instances))

    

def list_my_token_instances(list, tokens_database):
    for item in tokens_database[0]:
        custom_token_instance = Token(item, tokens_database)
        list.append(custom_token_instance)
    return list

def list_my_token_widget_instances(list_of_widgets, list_of_tokens, grid):
    for item in list_of_tokens:
        custom_widget_instance = TokenWidget(grid, 223, item)
        list_of_widgets.append(custom_widget_instance)
    return list_of_widgets

def redraw_back_main_page(win, tokens_database, token_instances=None):
    if type(token_instances) is list:
        clean_list_of_token_instances(token_instances) 
    for widget in list(win.widgets.values()):
        widget.destroy()
        del widget
    win.widgets.clear()
    win.canvas.delete('all')
    gc.collect()
    draw_buttons(win, tokens_database)
    pass

def clean_list_of_token_instances(list):
    for item in list:
        del item
    del list
    gc.collect()
    pass