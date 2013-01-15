#!/usr/bin/python
import os
import time
import urllib
from googlevoice import Voice 
from googlevoice.util import input

#logo print
def logo():
	print "PyScreenstuck - By Victor Barrera"
	print "================================="
	return

#Setting up logo
voice = Voice()
logo()

#Website RSS location
w_location = "http://www.mspaintadventures.com/rss/rss.xml"
w_rss = urllib.urlopen(w_location).read()

#Check if file exists
if os.path.isfile("savedate.txt") == 0:
	upd_loc = w_rss.find(";p=")
	upd_num = w_rss[upd_loc+3:upd_loc+9]
	file_open = open("savedate.txt", "w")
	file_open.write(upd_num+"\n")
	file_open.close()
	

	#Input for text and number
	phone_in = raw_input("Google Voice Number: ")
	text_in = raw_input("Text Message: ")
	while len(text_in) > 160:
		print "Error: Text Message over 160 characters"
		text_in = raw_input("Text Message: ")
				
	#Append to savedate data
	file_append = open("savedate.txt","a")
	file_append.write(phone_in+"\n")
	file_append.write(text_in)
	file_append.close()

#Timer
time_wait = 0
while 1:
		try:
			time_in = raw_input("Enter refresh time(in minutes): ")
			time_wait = int(time_in)
		except ValueError:
			print "Error: Not a number."
			continue
		else:
			if time_wait < 1:
				print "Error: Must be >=1."
				continue
			else:
				break
				
#Setup
file_read = open("savedate.txt", "r")
file_read.readline()
phoned = file_read.readline()
textd = file_read.readline()
while len(textd) > 160:
		print "Error: Text Message over 160 characters"
		textd = raw_input("Text Message: ")
file_read.close()
voice.login()

#Clear and run
os.system(['clear','cls'][os.name == 'nt'])
logo()
print "Now checking for updates..."

#Loop and check every specified minute
while 1:
	w_rss_new = urllib.urlopen(w_location).read()
	updl = w_rss_new.find(";p=")
	updn = w_rss_new[updl+3:updl+9]
	fopen = open("savedate.txt","r")
	check = fopen.readline()
	fopen.close()
	
	#Compare
	if check[:6] != updn[:6]:
		print "New Update!"
		#Send text
		voice.send_sms(phoned,textd)
		fopen_new = open("savedate.txt","w")
		fopen_new.write(updn+"\n")
		fopen_new.write(phoned)
		fopen_new.write(textd)
		fopen_new.close()


	#Sleep	
	time.sleep(60*time_wait)


