from pynput.keyboard import Listener, KeyCode
import time

# --- functions ---

def get_pressed(event):
    global key_a # inform function to use external/global variable instead of local one

    if event == KeyCode.from_char('a'):
        key_a = True

def get_released(event):
    global key_a

    if event == KeyCode.from_char('a'):
        key_a = False

# --- main --

key_a = False  # default value at start

listener = Listener(on_press=get_pressed, on_release=get_released)
listener.start() # start thread with listener

while True:

    if key_a:
        print('hold pressed: a')

    time.sleep(.1)  # slow down loop to use less CPU

listener.stop() # stop thread with listener
listener.join() # wait till thread ends work