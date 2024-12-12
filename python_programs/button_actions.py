import subprocess
from graphics import *

def draw_buttons(win):
    invitations = CustomButton(win, 'Invitations', "https://objkt.com/collections/KT1MFqZPJFhg5rUcW1VFxKrEKASMfsVg8Ukc",
    200, 250, (100, 50))
    invitations.draw()
    invitations.bind_click(lambda: open_webpage())
    forge = CustomButton(win, 'Forge', 'Forge process', 500, 250, (100, 50))
    forge.draw()
    forge.bind_click(lambda: redraw_forge(win))
    collection = CustomButton(win, 'Collection', 'Open collection', 700, 550, (85, 35))
    collection.draw()
    collection.bind_click(lambda: redraw_collection(win))
    settings = CustomButton(win, 'Settings', 'Open settings', 5, 545, (50, 50))
    settings.draw()
    #settings.bind_click(redraw_settings)
    pass


def open_webpage():
    subprocess.Popen(["brave-browser", "--password-store=basic", 
                      "https://objkt.com/collections/KT1MFqZPJFhg5rUcW1VFxKrEKASMfsVg8Ukc"])

def redraw_forge(win):
    win.canvas.delete('all')
    token_one = CustomButton(win, 'First token', 'Some link', 200, 250, (100, 50))
    token_one.draw()
    token_two = CustomButton(win, 'Second token', 'Some link', 500, 250, (100, 50))
    token_two.draw()
    accept_forge = CustomButton(win, 'Forge!', 'Some link', 350, 400, (100, 50))
    accept_forge.draw()
    back_button = CustomButton(win, 'Go back', 'Some link', 700, 550, (85, 35))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_main_page(win))
    pass

def redraw_collection(win):
    win.canvas.delete('all')

    #Frame for grid
    frame_grid = CustomFrame(win.canvas, 15, 60, 680, 423, True)
    win.widgets['frame_grid'] = frame_grid
    
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
    back_button.bind_click(lambda: redraw_back_main_page(win))

    #Test button inside the frame widget
    test_button = CustomButton(frame_grid, 'some text', 'some link', 3, 3, (40, 40))
    test_button.draw()

    #Test button2 inside the frame widget
    test_button2 = CustomButton(frame_grid, 'some text', 'some link', 3, 400, (40, 40))
    test_button2.draw()

    


    pass    

def redraw_back_main_page(win):
    for widget in list(win.widgets.values()):
        widget.destroy()
    win.widgets.clear()
    win.canvas.delete('all')
    draw_buttons(win)
    pass

