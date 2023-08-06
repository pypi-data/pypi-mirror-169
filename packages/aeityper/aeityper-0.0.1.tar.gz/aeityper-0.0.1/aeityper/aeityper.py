import keyboard  # using module keyboard
import time
import pyautogui
import pyperclip

def type(countdown, text):
    while countdown>0:
        print(countdown)
        countdown=countdown-1
        time.sleep(1)
    for i in text:
        pyautogui.press(i)
    

def listen():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('pagedown'):  # if key 'q' is pressed
                type(6,pyperclip.paste())
                print('You Pressed A Key!')
            if keyboard.is_pressed('pageup'):
                print('You pressed page up')
                break
        except:
            break  # if user pressed a key other than the given key the loop will break
