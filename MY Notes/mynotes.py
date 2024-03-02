from tkinter import *

color_bg = "white"
color_fg = "Black"
mnu_bg = "Black"


mainwindow = Tk()
mainwindow.geometry('350x200')
mainwindow.title("My Notes")
mainwindow.wm_resizable(False, False)


def Change_appearance(color_bg, color_fg):
    notesarea['bg'] = color_bg
    notesarea['fg'] = color_fg


def white_on_black():
    global mnu_bg
    color_bg = "Black"
    color_fg = "White"
    menubar['bg'] = mnu_bg
    Change_appearance(color_bg, color_fg)


def Default():
    global color_bg, color_bg, mnu_bg
    menubar['bg'] = mnu_bg
    Change_appearance(color_bg, color_fg)


def Black_on_orange():
    color_bg = "Orange"
    color_fg = "Black"
    menubar['bg'] = "green"
    Change_appearance(color_bg, color_fg)


def Change_color(Name, textcolor):
    notesarea.tag_configure(f"{Name}", foreground=textcolor)
    try:
        notesarea.tag_add(f"{Name}", "sel.first", "sel.last")
    except Exception as e:
        pass


def Color_green():
    Name = "green_color"
    text_color = "Green"
    Change_color(Name, text_color)


def Color_red():
    Name = "red_color"
    text_color = "Red"
    Change_color(Name, text_color)


def Color_blue():
    Name = "blue_color"
    text_color = "Blue"
    Change_color(Name, text_color)


menubar = Menu(mainwindow, bg=mnu_bg)
appearance = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Appearance', menu=appearance)
appearance.add_command(label="Default", command=Default)
appearance.add_command(label="White on black", command=white_on_black)
appearance.add_command(label="Black on orange", command=Black_on_orange)

Text_color = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Text Color', menu=Text_color)
Text_color.add_command(label="Green", command=Color_green)
Text_color.add_command(label="Red", command=Color_red)
Text_color.add_command(label="Blue", command=Color_blue)

mainwindow.configure(menu=menubar)

notesarea = Text(mainwindow, bg=color_bg, fg=color_fg, font="Ubuntu 15 bold")
notesarea.pack(fill=BOTH,)

mainwindow.mainloop()
