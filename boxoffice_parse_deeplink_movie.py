from bs4 import BeautifulSoup
import os
import pandas as pd
import glob
import datetime
import re

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()


for one_file_name in glob.glob("deep_link_movie_html/*.html"):
	print("parsing: ",one_file_name)
	scraping_time = os.path.basename(one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	bodybody = soup.find('body')
	summary_table = bodybody.find("div", {'class':'a-section a-spacing-none mojo-summary-values mojo-hidden-from-mobile'})
	spans = summary_table.find_all('span')
	movie_name = bodybody.find("h1", {'class':'a-size-extra-large'}).text
	# print(movie_name)
	# opening = summary_table.find("span",text=re.compile("Opening")).find_next('span').text
	openings = summary_table.find_all("span", {"class":"money"})
	if openings:
		opening = summary_table.find_all("span", {"class":"money"})[0].text.replace(",","").replace("$","")
	else:
   		opening = "N/A"	
	# print(opening)
	release_date = summary_table.find("span",text=re.compile("Release Date")).find_next('span').text
	# print(release_date)
	#MPAA = summary_table.find("span",text=re.compile("MPAA")).find_next('span').text
	MPAAs = summary_table.find("span",text=re.compile("MPAA"))
	if MPAAs:
		MPAA = summary_table.find("span",text=re.compile("MPAA")).find_next('span').text
	else:
   		MPAA = "N/A"
	# print(MPAA)
	#https://stackoverflow.com/questions/59397911/is-there-a-way-to-skip-attributeerror-nonetype-object-has-no-attribute-paren
	running_times= summary_table.find("span",text=re.compile("Running Time"))
	if running_times:
		running_time= summary_table.find("span",text=re.compile("Running Time")).find_next('span').text
		running_match = re.search(r"(\d+).*?(\d+)", running_time)
		if running_match:
			r_hour = int(running_match.group(1))
			r_min = round(int(running_match.group(2))/60,2)
		else:
	   		r_hour = "N/A"
	   		r_min = ""
		# r_hour = running_match.group(1)
	running_time_hour = r_hour + r_min
	# print(running_time_hour)
	#https://stackoverflow.com/questions/25914002/return-the-second-instance-of-a-regex-search-in-a-line
	# print(running_time)
	genres_s= summary_table.find("span",text=re.compile("Genres"))
	if genres_s:
		genres = summary_table.find("span",text=re.compile("Genres")).find_next('span').text
	else:
   		genres = "N/A"
	# print(genres)
	in_release_s = summary_table.find("span",text=re.compile("In Release"))
	if in_release_s:
		in_release_ = summary_table.find("span",text=re.compile("In Release")).find_next('span').text
		in_release = re.findall(r"[0-9]+", in_release_)[0]
	else:
   		in_release = "N/A"
	widest_release_s = summary_table.find("span",text=re.compile("Widest Release"))
	if widest_release_s:
		widest_release= summary_table.find("span",text=re.compile("Widest Release")).find_next('span').text.replace(" theaters","").replace(" theater","").replace(",","")
	else:
   		widest_release = "N/A"
	# print("in_release: " +in_release)
	# print("widest_release: " + widest_release)
	link = summary_table.find("span",text=re.compile("IMDbPro")).find_next('span').find('a')["href"]
	IMDB_ID = "tt"+re.findall(r"[0-9]+", link)[0]
	# print(IMDB_ID)

	df = df.append({  # df=data frame ( = put argumet, { = list of stuff
			'movie name':movie_name,
			'opening':opening,
			'release date':release_date,
			'MPAA':MPAA,
			'running time': running_time_hour,
			'genres':genres,
			'in release':in_release,
			'widest release':widest_release,
			'IMDB ID': IMDB_ID
		}, ignore_index=True)

df.to_csv("parsed_files/movie_web_deeplinks.csv")















