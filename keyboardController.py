from pynput.keyboard import Key, Controller
from pynput import keyboard
import string
from glosbe_mod import check_dictionary
from engkor_combined import *

my_keyboard = Controller()
word = []

def switch_input_source():
    my_keyboard.press(Key.ctrl)
    my_keyboard.press(Key.alt)
    my_keyboard.press(Key.up)
    my_keyboard.release(Key.up)
    my_keyboard.release(Key.ctrl)
    my_keyboard.release(Key.alt)

def delete_word(actual_word):
    for i in range(0, len(actual_word)+1):
        my_keyboard.press(Key.backspace)
        my_keyboard.release(Key.backspace)

def check_word(actual_word):
    (eng_valid, _) = check_dictionary(actual_word)
    #print(eng_valid, kor_valid)
    if (eng_valid == False):
        #korWord = engTypeToKor(actual_word)
        korWord = "여보"
        (_, kor_valid) = check_dictionary(korWord)
        if (kor_valid):
            print(actual_word)
            delete_word(actual_word) #deletes english word
            switch_input_source() #switches to korean keyboard
            my_keyboard.type(actual_word) #types out sequence
            switch_input_source() #switches back

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
        #print(actual_word)
        check_word(actual_word)
        print("cleared")
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
