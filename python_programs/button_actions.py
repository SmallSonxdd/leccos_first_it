import subprocess
from graphics import *

def draw_buttons(win):
    invitations = Button(win, 'Invitations', "https://objkt.com/collections/KT1MFqZPJFhg5rUcW1VFxKrEKASMfsVg8Ukc",
    200, 250, (100, 50))
    invitations.draw()
    invitations.bind_click(lambda: open_webpage())
    forge = Button(win, 'Forge', 'Forge process', 500, 250, (100, 50))
    forge.draw()
    forge.bind_click(lambda: redraw_forge(win))
    collection = Button(win, 'Collection', 'Open collection', 700, 550, (85, 35))
    collection.draw()
    collection.bind_click(lambda: redraw_collection(win))
    settings = Button(win, 'Settings', 'Open settings', 5, 545, (50, 50))
    settings.draw()
    #settings.bind_click(redraw_settings)
    pass


def open_webpage():
    subprocess.Popen(["brave-browser", "--password-store=basic", 
                      "https://objkt.com/collections/KT1MFqZPJFhg5rUcW1VFxKrEKASMfsVg8Ukc"])

def redraw_forge(win):
    win.canvas.delete('all')
    token_one = Button(win, 'First token', 'Some link', 200, 250, (100, 50))
    token_one.draw()
    token_two = Button(win, 'Second token', 'Some link', 500, 250, (100, 50))
    token_two.draw()
    accept_forge = Button(win, 'Forge!', 'Some link', 350, 400, (100, 50))
    accept_forge.draw()
    back_button = Button(win, 'Go back', 'Some link', 700, 550, (85, 35))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_main_page(win))
    pass

def redraw_collection(win):
    win.canvas.delete('all')
    
    #Scrollbar
    scrollbar = CustomScrollbar(win.canvas, "vertical", 700, 15, 85, 485)
    scrollbar.draw()
    scrollbar.set_command(win.canvas.yview)
    win.canvas.config(yscrollcommand=scrollbar.get_scrollbar().set)
    win.widgets['scrollbar'] = scrollbar


    #Search bar
    search_entry = CustomEntry(win.canvas, 15, 15, 630, 30)
    win.widgets['search_entry'] = search_entry

    #Clear button
    clear_button = Button(win, 'Clear', 'Some link', 645, 15, (50, 30))
    clear_button.draw()

    back_button = Button(win, 'Go back', 'Some link', 700, 500, (85, 85))
    back_button.draw()
    back_button.bind_click(lambda: redraw_back_main_page(win))
    pass    

def redraw_back_main_page(win):
    for widget in list(win.widgets.values()):
        widget.destroy()
    win.widgets.clear()
    win.canvas.delete('all')
    draw_buttons(win)
    pass

