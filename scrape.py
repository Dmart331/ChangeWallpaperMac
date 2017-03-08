import requests 
import shutil
import json
import time 
import datetime
import random





def crawl():

	r = requests.get('https://api.nasa.gov/planetary/apod?date={}&api_key=1HHTiK7TQC5QWyOMW2RTDnyuWSiDFYChaAues6PX'.format(date))
	print("Retreving Data")
	parsed = json.loads(r.content)
	print("LOOOOOOK HERRREEEEEE*********", parsed["url"])
	with open('/Users/paulmartin/change/newback/{}.jpg'.format(date), 'wb') as handle:
	        response = requests.get(parsed["url"])

	        if not response.ok:
	            print(response)

	        for block in response.iter_content(1024):
	            if not block:
	                break

	            handle.write(block)


start_date = "2011/01/23"
date = datetime.datetime.strptime(start_date, "%Y/%m/%d").date()
for i in range(364): 	 
	date += datetime.timedelta(days=1)
	print(date)



if __name__ == "__main__":
	print("""
		  Welcome! Choose an Option Below to change the background \n
		  to suit the mood you are in \n
		  1.Space\n
		  2.City\n
		  3.Nature\n
		  """)
	choice = input('>')
	if choice == '1':
		crawl()
