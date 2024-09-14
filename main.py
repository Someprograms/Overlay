import time

import keyboard
import re
import tkinter as tk
import threading
from pynput import keyboard as Keyboard
selectedKeys = ['a', 'b']
forloopIndex = 0
startCanvasThread = True
startCanvas2Thread = True


def on_key_release(key):

    if key.char == selectedKeys[0]:
        canvas.config(bg='white')
    elif key.char == selectedKeys[1]:
        canvas2.config(bg='white')


def changecanvascolor():
    canvas.config(bg='black')
    #time.sleep(0.1)
    #canvas.config(bg='white')



def changecanvascolor2():
    canvas2.config(bg='black')
    #time.sleep(0.1)
    #canvas2.config(bg='white')




def detectkeypress():
    print("text")
    while True:
        for i in range(len(selectedKeys)):
            val = selectedKeys[i]

            if keyboard.is_pressed(val) and i == 0:
                changecanvascolor()
                #t3 = threading.Thread(target=changecanvascolor)
                #if not t3.is_alive():
                    #t3.start()
                    #t3.join()
            elif keyboard.is_pressed(val) and i == 1:
                changecanvascolor2()

            #elif keyboard.release(val) and i == 0:
                #canvas.config(bg='white')
            #elif keyboard.release(val) and i == 1:
                #canvas2.config(bg='white')
                #if startCanvas2Thread:
                    #t4 = threading.Thread(target=changecanvascolor2)

                    #if not t4.is_alive():
                        #t4.start()
                        #t4.join()





def window():
    listener =  Keyboard.Listener(on_release=on_key_release)
    listener.start()

    win = tk.Tk()
    global canvas
    canvas = tk.Canvas(win, bg='green')
    canvas.grid(column=0, row=0)
    global canvas2
    canvas2 = tk.Canvas(win)
    canvas2.grid(column=1, row=0)

    tk.mainloop()


t2 = threading.Thread(target=detectkeypress)
t1 = threading.Thread(target=window)


t2.start()
t1.start()

t1.join()














