import tkinter as tk
import threading
from pynput import keyboard as Keyboard
import keyboard as kb
selectedKeys = []
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


    def addOrRemoveKey(self, addOrRemoveCanvas):
        global keys
        global canvas2
        global canvas
        global canvas3
        global canvas4
        if addOrRemoveCanvas == 'addCanvas':
            keys = keys + 1
            if keys == 1:
                canvas = tk.Canvas(win)
                canvas.grid(column=1, row=0)
                canvas.config(width=50, height=50)
            elif keys == 2:

                canvas2 = tk.Canvas(win)
                canvas2.grid(column=2, row=0)
                canvas2.config(width=50, height=50)
            elif keys == 3:
                canvas3 = tk.Canvas(win)
                canvas3.grid(column=3, row=0)
                canvas3.config(width=50, height=50)
            elif keys == 4:

                canvas4 = tk.Canvas(win)
                canvas4.grid(column=4, row=0)
                canvas4.config(width=50, height=50)
        elif addOrRemoveCanvas == 'removeCanvas':
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
            if key.char == selectedKeys[2]:
                if canvas3:
                    canvas3.delete(text_id3)
                    text_id3 = None
            if key.char == selectedKeys[3]:
                if canvas4:
                    canvas4.delete(text_id4)
                    text_id4 = None
            if key.char == selectedKeys[0]:
                if canvas:
                    canvas.delete(text_id)
                    text_id = None
            if key.char == selectedKeys[1]:
                if canvas2:
                    canvas2.delete(text_id2)
                    text_id2 = None
            else:
                print('this is some text')
        except:
            print('')


def window():

    #listener2 = Keyboard.Listener(on_press=on_key_press2)
    #listener2.start()
    global win
    win = tk.Tk()

    win.overrideredirect(True)
    win.wm_attributes("-topmost", 1)
    global deleteCanvasText
    def deleteCanvasText(variable, textID):
        variable.delete(textID)
    def options():
        global options1
        options1 = tk.Toplevel(win)
        #tk.Button(options1, text="Set keys", command=append).grid(row=0, column=2, sticky='nsew')
        tk.Button(options1, text="Add a key", command=lambda x='addCanvas', y='': addOrRemoveKeyClass.addOrRemoveKey(addOrRemoveCanvas=x,self=y)).grid(row=1, column=2, sticky='nsew')
        tk.Button(options1, text="Remove a key", command=lambda x='removeCanvas', y='': addOrRemoveKeyClass.addOrRemoveKey(addOrRemoveCanvas=x, self=y)).grid(row=2, column=2, sticky='nsew')
        text = tk.Text(options1)
        text.insert(index=0.0, chars='key 1')
        text.grid(column=0, row=0)
        text.config(width=10, height=1)
        text2 = tk.Text(options1)
        text2.insert(index=0.0, chars='key 2')
        text2.grid(column=0, row=1)
        text2.config(width=10, height=1)
        text3 = tk.Text(options1)
        text3.insert(index=0.0, chars='key 3')
        text3.grid(column=0, row=2)
        text3.config(width=10, height=1)
        text4 = tk.Text(options1)
        text4.insert(index=0.0, chars='key 4')
        text4.grid(column=0, row=3)
        text4.config(width=10, height=1)
        global menuOptions
        menuOptions = ['a', 'b', 'c', 'd']
        global selectedOption
        selectedOption = tk.StringVar()
        global menu
        menu = tk.OptionMenu(options1, selectedOption, *menuOptions, command=lambda x=selectedOption, y='menu': [selectedKeys.append(x), do_something(x, y)])

        menu.grid(column=1, row=0)
        global selectedOption2
        selectedOption2 = tk.StringVar()
        global menu2
        menu2 = tk.OptionMenu(options1, selectedOption2, *menuOptions,
                            command=lambda x=selectedOption2, y='menu2': [selectedKeys.append(x), do_something(x, y)])
        menu2.grid(column=1, row=1)
        global selectedOption3
        selectedOption3 = tk.StringVar()
        global menu3
        menu3 = tk.OptionMenu(options1, selectedOption3, *menuOptions,
                              command=lambda x=selectedOption3, y='menu3': [selectedKeys.append(x), do_something(x, y)])

        menu3.grid(column=1, row=2)
        global selectedOption4
        selectedOption4 = tk.StringVar()
        global menu4
        menu4 = tk.OptionMenu(options1, selectedOption4, *menuOptions,
                              command=lambda x=selectedOption4, y='menu4': [selectedKeys.append(x), do_something(x, y)])

        menu4.grid(column=1, row=3)


    tk.Button(win, text="Settings", command=options).grid(row=0, column=0, sticky='nsew')
    tk.mainloop()


def do_something(var, var2):
    global menuOptions
    global stringVar
    global menu
    global menu2
    global menu3
    global menu4
    global selectedOption
    if var2 == 'menu':
        options = menu['menu']
        options.delete(0, 'end')
        menuOptions.remove(var)
        for string in menuOptions:
            options.add_command(label=string, command = tk._setit(selectedOption, string, lambda x=selectedOption, y='menu': [selectedKeys.insert(0, x), do_something(x, y)]))
        menuOptions = ['a', 'b', 'c', 'd']
    elif var2 == 'menu2':

        options = menu2['menu']
        stringVar = selectedOption2
        options.delete(0, 'end')
        menuOptions.remove(var)
        for string in menuOptions:
            options.add_command(label=string, command = tk._setit(selectedOption2, string, lambda x=selectedOption, y='menu2': [selectedKeys.insert(1, x), do_something(x, y)]))
        menuOptions = ['a', 'b', 'c', 'd']
    elif var2 == 'menu3':

        options = menu3['menu']
        stringVar = selectedOption3
        options.delete(0, 'end')
        menuOptions.remove(var)
        for string in menuOptions:
            options.add_command(label=string, command = tk._setit(selectedOption3, string, lambda x=selectedOption, y='menu3': [selectedKeys.insert(2, x), do_something(x, y)]))
        menuOptions = ['a', 'b', 'c', 'd']
    elif var2 == 'menu4':
        options = menu4['menu']
        stringVar = selectedOption4
        options.delete(0, 'end')
        menuOptions.remove(var)
        for string in menuOptions:
            options.add_command(label=string, command = tk._setit(selectedOption4, string, lambda x=selectedOption, y='menu4': [selectedKeys.insert(3, x), do_something(x, y)]))
        menuOptions = ['a', 'b', 'c', 'd']


listener = Keyboard.Listener(on_press=on_key_press, on_release=on_release)
listener.start()
window()






















