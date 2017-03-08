import subprocess
import random
import time
import requests 
import shutil
import json
# from newback import *
import time 
import datetime
import random


# List of image names to be grabbed randomly and pushed to file location located in SCRIPT TODO: Find a cleaner way to do this


# Function to be called in name main with while true to have loop on interval

def strTimeProp(start, end, format, prop):
	stime = time.mktime(time.strptime(start, format))
	etime = time.mktime(time.strptime(end, format))

	ptime = stime + prop * (etime - stime)

	return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
	return strTimeProp(start, end, '%Y-%m-%d', prop)

def set_desktop_background_newback():
	folders = ["SpaceCollectionOne", "SpaceCollectionTwo"]

	folder = random.choice(folders)

	start_date = ""

	if folder == "SpaceCollectionOne":
		start_date = randomDate("2011-01-01", "2011-01-22", random.random())

	if folder == "SpaceCollectionTwo":
		start_date = randomDate("2016-01-01", "2016-04-12", random.random())


	SCRIPT1 = """
	osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/paulmartin/change/{}/{}.jpg" '
	""".format(folder, start_date)
	subprocess.Popen(SCRIPT1, shell=True)

def set_desktop_background_nature():
	images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg' , '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg', '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg', '38.jpg', '39.jpg', '40.jpg', '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '50.jpg']

	SCRIPT2 = """
	osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/paulmartin/change/Nature/{}" '
	""".format(random.choice(images))

	subprocess.Popen(SCRIPT2, shell=True);






# Do the thing
if __name__ == '__main__':

	print("Welcome to Wallpaper Changer! Select an option to get started!")
	print("""
			1. Space Wallpapers\n
			2. Nature Wallpapers
			""")
	choice = input('>')

	if choice == '1':
		while True:
			set_desktop_background_newback()
			time.sleep(3)
	if choice == '2':
		while True:
			set_desktop_background_nature()
			time.sleep(3)
	# while True:
	# 	set_desktop_background()
	# 	# 900 is 15 minutes. change as you desire.
	# 	time.sleep(3)

