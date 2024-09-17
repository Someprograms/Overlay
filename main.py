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
        win.update_idletasks()
        options1.update_idletasks()
        global keys
        global canvas2
        if addOrRemoveCanvas == 'addCanvas':
            keys = keys + 1
            if keys == 2:

                canvas2 = tk.Canvas(win)
                canvas2.grid(column=2, row=0)
                canvas2.config(width=50, height=50)
        elif addOrRemoveCanvas == 'removeCanvas':
            keys = keys - 1
        print(keys)
        
        if keys == 1:
            try:
                canvas2.destroy()
                del canvas2
                print('canvas2 has been destroyed')
            except:
                print('canvas2 is undefined')
            print('canvas')
            global canvas
            canvas = tk.Canvas(win)
            canvas.grid(column=1, row=0)
            canvas.config(width=50, height=50)
        else:
            print('')




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
        tk.Button(options1, text="Add key", command=lambda x='addCanvas', y='': addOrRemoveKeyClass.addOrRemoveKey(addOrRemoveCanvas=x,self=y)).grid(row=1, column=2, sticky='nsew')
        tk.Button(options1, text="Remove key", command=lambda x='removeCanvas', y='': addOrRemoveKeyClass.addOrRemoveKey(addOrRemoveCanvas=x, self=y)).grid(row=2, column=2, sticky='nsew')
        text = tk.Text(options1)
        text.insert(index=0.0, chars='key 1')
        text.grid(column=0, row=0)
        text.config(width=10, height=1)
        text2 = tk.Text(options1)
        text2.insert(index=0.0, chars='key 2')
        text2.grid(column=0, row=1)
        text2.config(width=10, height=1)
        global entry
        entry = tk.Entry(options1)
        entry.grid(column=1, row=0)
        entry.config()
        global entry2
        entry2 = tk.Entry(options1)
        entry2.grid(column=1, row=1)
        entry2.config()
    tk.Button(win, text="Settings", command=options).grid(row=0, column=0, sticky='nsew')
    win.update_idletasks()
    tk.mainloop()


def append():
    selectedKeys.clear()
    selectedKeys.append(entry.get())
    selectedKeys.append(entry2.get())
    print(selectedKeys)

t1 = threading.Thread(target=window)
t1.start()


t1.join()














