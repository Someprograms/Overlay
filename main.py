import tkinter as tk
import threading
from pynput import keyboard as Keyboard
selectedKeys = []
forloopIndex = 0
startCanvasThread = True
startCanvas2Thread = True


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




def window():
    listener = Keyboard.Listener(on_release=on_key_release, on_press=on_key_press)
    listener.start()
    win = tk.Tk()
    global canvas
    canvas = tk.Canvas(win)
    canvas.grid(column=2, row=0)
    canvas.config(width=50, height=50)
    global entry
    entry = tk.Entry(win)
    entry.grid(column=1, row=0)
    entry.config()
    text = tk.Text()
    text.insert(index=0.0, chars='key 1')
    text.grid(column=0, row=0)
    text.config(width=10, height=1)
    text2 = tk.Text()
    text2.insert(index=0.0, chars='key 2')
    win.overrideredirect(True)
    text2.grid(column=0, row=1)
    text2.config(width=10, height=1)
    global entry2
    entry2 = tk.Entry(win)
    entry2.grid(column=1, row=1)
    entry2.config()
    global canvas2
    canvas2 = tk.Canvas(win)
    canvas2.grid(column=3, row=0)
    canvas2.config(width=50, height=50)
    tk.Button(win, text="Set keys", command=append).grid(row=1, column=2, sticky='nsew')
    win.wm_attributes("-topmost", 1)
    tk.mainloop()


def append():
    selectedKeys.clear()
    selectedKeys.append(entry.get())
    selectedKeys.append(entry2.get())
    print(selectedKeys)

t1 = threading.Thread(target=window)
t1.start()


t1.join()














