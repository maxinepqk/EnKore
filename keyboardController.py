from pynput.keyboard import Key, Controller
from pynput import keyboard
import string
from glosbe_mod import converter

my_keyboard = Controller()
word = []

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(key))
    if (key == keyboard.Key.space):
        actual_word = ''.join(word)
        print(actual_word)
        (eng_valid, kor_valid) = converter(actual_word)
        word.clear()
        print(eng_valid, kor_valid)
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
