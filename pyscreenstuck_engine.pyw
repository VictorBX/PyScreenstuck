#!/usr/bin/python
import os
import time
import urllib
from googlevoice import Voice 
from googlevoice.util import input

class engine:
	def __init__(self):
		self.control = 0

	def change(self):
		self.control = 1 
	
	def setup(self,emailp,passp,phonep):
		self.check_file()
		self.keep_checking(emailp,passp,phonep)

	def check_file(self):
		if os.path.isfile("savedate.txt") == 0:
			w_location = "http://www.mspaintadventures.com/rss/rss.xml"
			w_rss = urllib.urlopen(w_location).read()
			upd_loc = w_rss.find(";p=")
			upd_num = w_rss[upd_loc+3:upd_loc+9]
			file_open = open("savedate.txt", "w")
			file_open.write(upd_num)
			file_open.close()

	def keep_checking(self,emaild,passd,phoned):
		voice = Voice()
		voice.login(emaild,passd)
			
		while self.control == 0:
			w_location = "http://www.mspaintadventures.com/rss/rss.xml"
			w_rss_new = urllib.urlopen(w_location).read()
			updl = w_rss_new.find(";p=")
			updn = w_rss_new[updl+3:updl+9]
			fopen = open("savedate.txt","r")
			check = fopen.readline()
			fopen.close()

			#Compare
			if check[:6] != updn[:6]:
				#Send text
				voice.send_sms(phoned,"HOMESTUCK!")
				fopen_new = open("savedate.txt","w")
				fopen_new.write(updn)
				fopen_new.close()

			#Sleep	
			for i in range(60):
				if self.control == 0:
					time.sleep(1)