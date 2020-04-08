
import urllib.request
import time
import datetime
import os    #allows working with folders in python


if not os.path.exists("html_files"):
    os.mkdir("html_files")

years = ["2017", "2016", "2005", "2004", "1994", "1993", "1992"]

for y in years:
	print("requesting:" + y) 
	if os.path.exists("html_files/boxoffice" + y + ".html"):
		print(y + " exists")
	else:
		f = open("html_files/boxoffice" + y + ".html", "wb") 
		response = urllib.request.urlopen('https://www.boxofficemojo.com/daily/'+ y +'/?view=year')
		html = response.read()#saving the text part of the page in this variable
		f.write(html)#making sure that the file name will be different everytime that we save the file.
		f.close()
		time.sleep(10)#the time is in seconds and increase the number to avoid website blockage



#w here means that we want to write it. b means binary.
#we usually need to have the open command in the beginning of the programm



