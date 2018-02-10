from pynput.keyboard import Key, Controller
from pynput import keyboard
import string

my_keyboard = Controller()
word = []

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(key))
    if (key == keyboard.Key.space):
        print(word)
        # send u the word 
        word.clear()
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    try:
        word.append(key.char)
    except AttributeError:
        print("")

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
