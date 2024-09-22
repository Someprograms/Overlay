import customtkinter as tk
import threading
from pynput import keyboard as Keyboard
import keyboard as kb
selectedKeys = ['', '', '', '']
forloopIndex = 0
startCanvasThread = True
startCanvas2Thread = True
openOptions = False
keys = 0
global canvas2
global text_id
global text_id2
global text_id3
global text_id4


def on_key_press(key):
    if key == Keyboard.Key.esc:
        win.destroy()
        quit()
    if selectedKeys:
        try:
            if key.char == selectedKeys[0]:
                global text_id
                if not globals().get('text_id'):
                   text_id = canvas.create_text(25, 25, text=selectedKeys[0].upper(), font='Rosemary 15')
            if key.char == selectedKeys[1]:
                global text_id2
                if not globals().get('text_id2'):
                    text_id2 = canvas2.create_text(25, 25, text=selectedKeys[1].upper(), font='Rosemary 15')
            if key.char == selectedKeys[2]:
                global text_id3
                if not globals().get('text_id3'):
                    text_id3 = canvas3.create_text(25, 25, text=selectedKeys[2].upper(), font='Rosemary 15')
            if key.char == selectedKeys[3]:
                global text_id4
                if not globals().get('text_id4'):
                    text_id4 = canvas4.create_text(25, 25, text=selectedKeys[3].upper(), font='Rosemary 15')

        except:
            print('')

class addOrRemoveKeyClass:
    def add_or_remove_key(self, addOrRemoveCanvas):
        global keys
        global canvas2
        global canvas
        global canvas3
        global canvas4
        if addOrRemoveCanvas == 'addCanvas':
            if keys < 4:
                keys = keys + 1
                print(keys)
                if keys == 1:
                    canvas = tk.CTkCanvas(master=win, background='#d4d4d4', highlightthickness=0)
                    canvas.grid(column=1, row=0)
                    canvas.config(width=50, height=50)
                elif keys == 2:

                    canvas2 = tk.CTkCanvas(master=win, background='#d4d4d4', highlightthickness=0)
                    canvas2.grid(column=2, row=0)
                    canvas2.config(width=50, height=50)
                elif keys == 3:
                    canvas3 = tk.CTkCanvas(master=win, background='#d4d4d4', highlightthickness=0)
                    canvas3.grid(column=3, row=0)
                    canvas3.config(width=50, height=50)
                elif keys == 4:

                    canvas4 = tk.CTkCanvas(master=win, background='#d4d4d4', highlightthickness=0)
                    canvas4.grid(column=4, row=0)
                    canvas4.config(width=50, height=50)
        elif addOrRemoveCanvas == 'removeCanvas':
            if keys > 0:
                keys = keys - 1
                if keys == 0:
                    try:
                        canvas.destroy()
                        print('canvas has been destroyed')
                    except:
                        print('canvas is undefined')
                if keys == 1:
                    try:
                        canvas2.destroy()
                        print('canvas2 has been destroyed')
                    except:
                        print('canvas2 is undefined')
                if keys == 2:
                    try:
                        canvas3.destroy()
                        print('canvas3 has been destroyed')
                    except:
                        print('canvas3 is undefined')
                if keys == 3:
                    try:
                        canvas4.destroy()
                        print('canvas4 has been destroyed')
                    except:
                        print('canvas4 is undefined')



def on_release(key):
    global text_id3
    global text_id
    global text_id2
    global text_id4
    if selectedKeys:
        try:
            if key.char == selectedKeys[0]:
                if canvas:
                    canvas.delete(text_id)
                    text_id = None
            if key.char == selectedKeys[1]:
                if canvas2:
                    canvas2.delete(text_id2)
                    text_id2 = None
            if key.char == selectedKeys[2]:
                if canvas3:
                    canvas3.delete(text_id3)
                    text_id3 = None
            if key.char == selectedKeys[3]:
                if canvas4:
                    canvas4.delete(text_id4)
                    text_id4 = None


            else:
                print('this is some text')
        except:
            print('')


def window():

    #listener2 = Keyboard.Listener(on_press=on_key_press2)
    #listener2.start()
    global win
    win = tk.CTk()

    win.geometry('+0+0')
    win.overrideredirect(True)
    win.wm_attributes("-topmost", 1)


    global deleteCanvasText
    def deleteCanvasText(variable, textID):
        variable.delete(textID)
    def options():
        tk.FontManager.load_font("Futura.ttf")
        global options1
        options1 = tk.CTkToplevel(win)
        options1.configure(fg_color='#feffed')
        options1.title('Settings')
        tk.CTkButton(options1, text="Add a key overlay", command=lambda x='addCanvas', y='': addOrRemoveKeyClass.add_or_remove_key(addOrRemoveCanvas=x,self=y)).grid(row=0, column=2, sticky='nsew', pady=(10,10))
        tk.CTkButton(options1, text="Remove a key overlay", command=lambda x='removeCanvas', y='': addOrRemoveKeyClass.add_or_remove_key(addOrRemoveCanvas=x, self=y)).grid(row=1, column=2, sticky='nsew', pady=(10,10))
        text = tk.CTkLabel(master=options1, width=20, height=20, text='KEY 1', font=('Futura', 14))
        text.grid(column=0, row=0, pady=(5, 5))
        text.configure(width=5, height=1)
        text2 = tk.CTkLabel(master=options1, width=20, height=20, text='KEY 2', font=('Futura', 14))
        text2.grid(column=0, row=1, pady=(5, 5))
        text2.configure(width=5, height=1)
        text3 = tk.CTkLabel(master=options1, width=20, height=20, text='KEY 3', font=('Futura', 14))
        text3.grid(column=0, row=2,pady=(5, 5))
        text3.configure(width=5, height=1)
        text4 = tk.CTkLabel(master=options1, width=20, height=20, text='KEY 4', font=('Futura', 14))
        text4.grid(column=0, row=3, pady=(5, 5))
        text4.configure(width=5, height=1)
        global menuOptions
        menuOptions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        global selectedOption
        selectedOption = tk.StringVar()
        selectedOption.set(selectedKeys[0])
        global menu
        menu = tk.CTkOptionMenu(master=options1,  variable=selectedOption, values=menuOptions, command=lambda x=selectedOption, y='menu': [selectedKeys.insert(0, x), do_something(x, y)], fg_color='#E0FFFF', text_color='black')
        menu.grid(column=1, row=0, pady=10, padx=(5, 5))
        global selectedOption2
        selectedOption2 = tk.StringVar()
        selectedOption2.set(selectedKeys[1])
        global menu2
        menu2 = tk.CTkOptionMenu(master=options1,variable=selectedOption2, values=menuOptions,
                            command=lambda x=selectedOption2, y='menu2': [selectedKeys.insert(1, x), do_something(x, y)], fg_color='#E0FFFF', text_color='black')
        menu2.grid(column=1, row=1, pady=10, padx=(5, 5))
        global selectedOption3
        selectedOption3 = tk.StringVar()
        selectedOption3.set(selectedKeys[2])
        global menu3
        menu3 = tk.CTkOptionMenu(master=options1, variable=selectedOption3, values=menuOptions,
                              command=lambda x=selectedOption3, y='menu3': [selectedKeys.insert(2, x), do_something(x, y)], fg_color='#E0FFFF', text_color='black')

        menu3.grid(column=1, row=2, pady=10, padx=(5, 5))
        global selectedOption4
        selectedOption4 = tk.StringVar()
        selectedOption4.set(selectedKeys[3])
        global menu4
        menu4 = tk.CTkOptionMenu(master=options1, variable=selectedOption4, values=menuOptions,
                              command=lambda x=selectedOption4, y='menu4': [selectedKeys.insert(3, x), do_something(x, y)], fg_color='#E0FFFF', text_color='black')

        menu4.grid(column=1, row=3, pady=10, padx=(5, 5))
    tk.CTkButton(win, corner_radius=0, bg_color='black', width=20, height=20, text="Settings", command=options).grid(row=0, column=0, sticky='nsew')
    win.mainloop()


def do_something(var, var2):
    global menuOptions
    global stringVar
    global menu
    global menu2
    global menu3
    global menu4
    global selectedOption
    if var2 == 'menu':
        menuOptions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        options = menuOptions
        options.remove(var)
        menu.configure(values=options)
    elif var2 == 'menu2':
        menuOptions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        options = menuOptions
        options.remove(var)
        menu2.configure(values=options)
    elif var2 == 'menu3':
        menuOptions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        options = menuOptions
        options.remove(var)
        menu3.configure(values=options)
    elif var2 == 'menu4':
        menuOptions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        options = menuOptions
        options.remove(var)
        menu4.configure(values=options)


listener = Keyboard.Listener(on_press=on_key_press, on_release=on_release)
listener.start()
window()






















