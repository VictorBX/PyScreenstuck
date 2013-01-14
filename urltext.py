import os
import time
import urllib
from googlevoice import Voice 
from googlevoice.util import input

#Setting up login info
voice = Voice()
voice.login("email here", "password here")

#Phone number and text
phoneNumber = "phone-number-here"
text = "Homestuck Upd8!"

#Website RSS location
w_location = "http://www.mspaintadventures.com/rss/rss.xml"
w_rss = urllib.urlopen(w_location).read()

#Input for timer
time_wait = 0
while 1:
	try:
		time_in = raw_input("Enter refresh time(in minutes): ")
		time_wait = int(time_in)
	except ValueError:
		print "Not a number."
		continue
	else:
		if time_wait < 1:
			print "Must be >=1."
			continue
		else:
			break

#Check if file exists
if os.path.isfile("savedate.txt") == 0:
	upd_loc = w_rss.find(";p=")
	upd_num = w_rss[upd_loc+3:upd_loc+9]
	file_open = open("savedate.txt", "w")
	file_open.write(upd_num)
	file_open.close()

#Loop and check every specified minute
while 1:
	w_rss_new = urllib.urlopen(w_location).read()
	updl = w_rss_new.find(";p=")
	updn = w_rss_new[updl+3:updl+9]
	fopen = open("savedate.txt","r")
	check = fopen.readline()
	fopen.close()
	
	#Compare
	if check != updn:
		print "New Update!"
		#Send text
		voice.send_sms(phoneNumber,text)
		fopen_new = open("savedate.txt","w")
		fopen_new.write(updn)
		fopen_new.close()

	#Sleep	
	time.sleep(60*time_wait)


