import subprocess
import gc
from graphics import *
from tarot_generation import *
from T2_generation import *

def draw_buttons(win, tokens_database):
    win.canvas.delete('all')
    clean_widgets(win)
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
    entry_token_one = CustomEntry(win.canvas, 200, 320, 100, 30)
    win.widgets['entry_one'] = entry_token_one
    token_two = CustomButton(win, 'Second token', 'Some link', 500, 250, (100, 50))
    token_two.draw()
    entry_token_two = CustomEntry(win.canvas, 500, 320, 100, 30)
    win.widgets['entry_two'] = entry_token_two
    accept_forge = CustomButton(win, 'Forge!', 'Some link', 350, 400, (100, 50))
    accept_forge.draw()
    accept_forge.bind_click(lambda: redraw_forge_process_tokens(win, tokens_database, entry_token_one.custom_get(), entry_token_two.custom_get()))
    back_button = CustomButton(win, 'Go back', 'Some link', 700, 550, (85, 35))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_main_page(win, tokens_database))
    pass

def redraw_forge_process_tokens(win, tokens_database, token_one, token_two):
    #this will need to be turned into helper functions to clean up
    if token_one == token_two:
        print("You've tried putting in the same token twice. Try again!")
        return
    token_one_existence = False
    token_two_existence = False
    for key in tokens_database[0]:
        if tokens_database[1][key][2] == token_one:
            token_one_existence = True
            placeholder_token_one = key
        if tokens_database[1][key][2] == token_two:
            token_two_existence = True
            placeholder_token_two = key
    if token_one_existence == False or token_two_existence == False:
        print(f'First token is {token_one_existence} and second token is {token_two_existence}')
        return
    token_one_validity = True
    token_two_validity = True
    if tokens_database[1][placeholder_token_one][3] == 'Depleted':
        print('First token invalid!')
        token_one_validity = False
    if tokens_database[1][placeholder_token_two][3] == 'Depleted':
            token_two_validity = False
            print('Second token invalid!')
    if token_one_validity == False or token_two_validity == False:
        print(f"First token's validity is {token_one_validity} and second token's validity is {token_two_validity}")
        return
    else:
        print('Both tokens are valid and we can proceed!')
    redraw_forge_tarot(win, tokens_database, placeholder_token_one, placeholder_token_two)    
    pass

    #here's the fun part
def redraw_forge_tarot(win, tokens_database, token_one, token_two):    
    win.canvas.delete('all')
    clean_widgets(win)

    list_of_tarots = list_my_tarot_instances([], populate_tarots(3))
    #Grid for tarot widgets
    my_grid = GridWidget(win.canvas, 50, 0, 250, 500, len(list_of_tarots))
    list_of_tarot_widget_instances = list_my_tarot_widget_instances([], list_of_tarots, my_grid)
    my_grid.add_multiple_items(list_of_tarot_widget_instances)
    my_grid.draw()
    for item in my_grid.grid_items:
        item.bind_click(lambda tarot=item.tarot: redraw_forge_finalisation(win, tokens_database, token_one, token_two, tarot))

    #Back button
    back_button = CustomButton(win, 'Go back', 'Some link', 700, 550, (85, 35))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_forge(win, tokens_database))
    pass
    
def redraw_forge_finalisation(win, tokens_database, token_one, token_two, tarot):
    win.canvas.delete('all')
    new_token = generate_T2_token(tokens_database, token_one, token_two, tarot)
    tokens_database[0].append(new_token[0])
    tokens_database[1][new_token[0]] = new_token[1:]

    #Back button1
    back_button = CustomButton(win, 'Go back to the forge!', 'Some link', 15, 550, (170, 35))
    back_button.draw()
    back_button.bind_click(lambda: redraw_forge(win, tokens_database))
    
    #Back button2
    back_button = CustomButton(win, 'Go back to main menu!', 'Some link', 615, 550, (170, 35))
    back_button.draw()
    back_button.bind_click(lambda: draw_buttons(win, tokens_database))
    pass

def redraw_collection(win, tokens_database):
    win.canvas.delete('all')
    list_of_token_instances = list_my_token_instances([], tokens_database)

    #Frame for grid
    frame_grid = CustomFrame(win.canvas, 15, 60, 678, 423, True)
    win.widgets['frame_grid'] = frame_grid
    
    #Grid for token widgets
    my_grid = GridWidget(frame_grid.canvas, 0, 0, 226, 300, 3)
    list_of_token_widget_instances = list_my_token_widget_instances([], list_of_token_instances, my_grid)
    my_grid.add_multiple_items(list_of_token_widget_instances)
    my_grid.draw()

    #Scrollbar - only works when mouse is over it for scrollwheel with mouse, up and down buttons work properly
    scrollbar = CustomScrollbar(win.canvas, "vertical", 700, 15, 85, 470)
    scrollbar.draw()
    scrollbar.set_command(frame_grid.canvas.yview)
    frame_grid.canvas.config(yscrollcommand=scrollbar.get_scrollbar().set)
    win.widgets['scrollbar'] = scrollbar

    #Search bar - currently doesn't "search" the frame or the grid for particular tokens
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
    pass
    

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

def list_my_tarot_instances(list, list_of_tarots_3_tuples):
    for item in list_of_tarots_3_tuples:
        custom_tarot_instance = Tarot(item, f'{item[0]}.jpg')
        list.append(custom_tarot_instance)
    return list

def list_my_tarot_widget_instances(list_of_widgets, list_of_tarots, grid):
    for item in list_of_tarots:
        custom_widget_instance = TarotWidget(grid, 200, 350, item)
        list_of_widgets.append(custom_widget_instance)
    return list_of_widgets

def redraw_back_main_page(win, tokens_database, token_instances=None):
    if type(token_instances) is list:
        clean_list_of_token_instances(token_instances) 
    clean_widgets(win)
    win.widgets.clear()
    win.canvas.delete('all')
    gc.collect()
    draw_buttons(win, tokens_database)
    pass

def redraw_back_forge(win, tokens_database):
    clean_widgets(win)
    redraw_forge(win, tokens_database)
    pass

def clean_list_of_token_instances(list):
    for item in list:
        del item
    del list
    gc.collect()
    pass

def clean_widgets(win):
    for widget in list(win.widgets.values()):
        widget.destroy()
        del widget
    gc.collect()
    pass