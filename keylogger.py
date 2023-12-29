#Install pynput
from pynput.keyboard import Key, Listener

# Reference https://pypi.org/project/pynput/
def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press = on_press ,on_release = on_release) as listener:
    listener.join()