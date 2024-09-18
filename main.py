import tkinter as tk
import threading
from pynput import keyboard as Keyboard
selectedKeys = []
forloopIndex = 0
startCanvasThread = True
startCanvas2Thread = True
openOptions = False
keys = 0
global canvas2
global menuOptions
menuOptions = ['a', 'b', 'c', 'd']

def on_key_release(key):
    if selectedKeys:
        try:
            if key.char == selectedKeys[0]:
                canvas.delete(text_id)
            elif key.char == selectedKeys[1]:
                canvas2.delete(text_id2)
        except:
            print('')


def on_key_press(key):
    if selectedKeys:
        print(selectedKeys)
        try:
            if key.char == selectedKeys[0]:
                global text_id
                text_id = canvas.create_text(25,25, text=selectedKeys[0].upper(), font='Rosemary 15')
            elif key.char == selectedKeys[1]:
                global text_id2
                text_id2 = canvas2.create_text(25, 25, text=selectedKeys[1].upper(), font='Rosemary 15')
        except:
            print('')


def OpenOptionsMenu():
    global openOptions
    openOptions = True

class addOrRemoveKeyClass:



    def addOrRemoveKey(self, addOrRemoveCanvas):
        global keys
        global canvas2
        global canvas
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
        elif addOrRemoveCanvas == 'removeCanvas':
            keys = keys - 1
            if keys == 0:
                try:
                    canvas.destroy()
                    del canvas
                    print('canvas has been destroyed')
                except:
                    print('canvas is undefined')
            if keys == 1:
                try:
                    canvas2.destroy()
                    del canvas2
                    print('canvas2 has been destroyed')
                except:
                    print('canvas2 is undefined')
        print(keys)





def removekey():

    global keys
    keys = keys - 1
    print(keys)


def window():
    listener = Keyboard.Listener(on_release=on_key_release, on_press=on_key_press)
    listener.start()
    global win
    win = tk.Tk()

    win.overrideredirect(True)
    win.wm_attributes("-topmost", 1)

    def options():
        global options1
        options1 = tk.Toplevel(win)
        tk.Button(options1, text="Set keys", command=append).grid(row=0, column=2, sticky='nsew')
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

        selectedOption = tk.StringVar()
        global menu
        menu = tk.OptionMenu(options1, selectedOption, *menuOptions, command=lambda x=selectedOption: [selectedKeys.append(x), dosomething()])

        menu.grid(column=1, row=0)
        selectedOption2 = tk.StringVar()
        global menu2
        menu2 = tk.OptionMenu(options1, selectedOption2, *menuOptions,
                             command=lambda x=selectedOption2: [selectedKeys.append(x), dosomething()])
        menu2.grid(column=1, row=1)
        selectedOption3 = tk.StringVar()
        global menu3
        menu3 = tk.OptionMenu(options1, selectedOption3, *menuOptions,
                              command=lambda x=selectedOption3: [selectedKeys.append(x), dosomething()])

        menu3.grid(column=1, row=2)
        selectedOption4 = tk.StringVar()
        global menu4
        menu4 = tk.OptionMenu(options1, selectedOption4, *menuOptions,
                              command=lambda x=selectedOption4: [selectedKeys.append(x), dosomething()])

        menu4.grid(column=1, row=3)
        #global entry
        #entry = tk.Entry(options1)
        #entry.grid(column=1, row=0)
        #entry.config()
        #global entry2
        #entry2 = tk.Entry(options1)
        #entry2.grid(column=1, row=1)
        #entry2.config()

    tk.Button(win, text="Settings", command=options).grid(row=0, column=0, sticky='nsew')
    tk.mainloop()


def append():
    #selectedKeys.clear()
    #selectedKeys.append(entry.get())
    #selectedKeys.append(entry2.get())
    print(selectedKeys)
def dosomething():
    for option in menuOptions:
        if option in selectedKeys:
            print('text')
            menuOptions.remove(option)
            print(menuOptions)
            return menuOptions







t1 = threading.Thread(target=window)
t1.start()
t2 = threading.Thread()


t1.join()














