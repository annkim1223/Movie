from bs4 import BeautifulSoup
import os
import pandas as pd
import glob
import lxml

if not os.path.exists("parse_files"):
  	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing: ",one_file_name)
	scraping_time = os.path.basename(one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	boxoffice_table = soup.find(id="table")
	boxoffice_rows = boxoffice_table.find_all("tr")
	for r in boxoffice_rows[1:]:
		boxoffice_links = r.find("a", {"class":"a-link-normal"})["href"]
		print(boxoffice_links)
		df = df.append({  # df=data frame ( = put argumet, { = list of stuff
				'link': boxoffice_links 
			}, ignore_index=True)


	print (df)

df.to_csv("parsed_files/boxoffice_links.csv")

# Python coinmarketcap_parse(new).py
"""
By doing so, you can do multiple rows by using code for one row in the loop function
When you print them, we can the list of name, price market cap, supply.
Catch is using "find_all" and using "loop" function.


Now, you have the text data you got from python. Now, we want to put it in CSV file. In csv file, you need to put "" to be able to indivate it is the column. 

Also, you import os and make a new folder to store the out put of out file.
"""



"""

2/6/2020
try to lean beautilful soup by looking at the documentation. 
Also, each website has different html structure so you need to use different code
for each website. You can practice it by repeating the code and looking at the html directly. 
But you can also inspect in the website. 


"""