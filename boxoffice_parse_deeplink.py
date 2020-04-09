from bs4 import BeautifulSoup
import os
import pandas as pd
import glob
import datetime

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("deep_link_html/*.html"):
	print("parsing: ",one_file_name)
	scraping_time = os.path.basename(one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	daily_table = soup.find(id='table')
	daily_rows = daily_table.find_all("tr")
	page_date = soup.find("div", {"class":"a-section a-spacing-none"}).find("h1").text.replace("Domestic Box Office For ","").replace(",","")		
	formatted_date = datetime.datetime.strptime(page_date, '%b %d %Y').strftime('%m/%d/%Y')
	for r in daily_rows[1:]:
		boxoffice_date = formatted_date
		movie_links = r.find("a", {"class":"a-link-normal"})["href"]
		movie_name = r.find("td", {"class":"a-text-left mojo-field-type-release mojo-cell-wide"}).find("a").text
		movie_dailygross = r.find("td", {"class":"a-text-right mojo-field-type-money mojo-estimatable"}).text.replace(",","").replace("$","")
		movie_theaters = r.find("td", {"class":"a-text-right mojo-field-type-positive_integer mojo-estimatable"}).text.replace(",","")
		movie_grosstodate = r.find_all("td", {"class":"a-text-right mojo-field-type-money mojo-estimatable"})[2].text.replace(",","").replace("$","")
		# movie_daynumber = r.find("td", {"class":"a-text-right mojo-field-type-positive_integer"}).text
		days_number = r.find_all("td", {"class":"a-text-right mojo-field-type-positive_integer"})
		movie_daynumber = days_number[1].text
		movie_distributor = r.find("td", {"class": "a-text-left mojo-field-type-release_studios"}).text

		df = df.append({  # df=data frame ( = put argumet, { = list of stuff
				'Date':boxoffice_date,
				'movie name':movie_name,
				'daily box office':movie_dailygross,
				'theaters': movie_theaters,
				'gross box office to date':movie_grosstodate,
				'number of days in release':movie_daynumber,
				'distributor': movie_distributor,
				'movie_links ': movie_links 

			}, ignore_index=True)
# 	# except:
# 	# 	pass

df.to_csv("parsed_files/movie_deeplinks.csv")













