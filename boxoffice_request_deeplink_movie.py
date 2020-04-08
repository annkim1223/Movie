import urllib.request
import os
import time
import pandas as pd
import re

if not os.path.exists("deep_link_movie_html"):
	os.mkdir("deep_link_movie_html")

df = pd.read_csv("parsed_files/movie_deeplinks.csv")

# print(df)

for link in df['movie_links ']:
	filename = re.findall(r"[0-9]+", link)[0]
	if os.path.exists("deep_link_movie_html/" + filename + ".html"):
		print(filename + " exists")
	else:
		print("Downloading: ", filename)	
		f = open("deep_link_movie_html/" + filename + ".html.temp", "wb")
		response = urllib.request.urlopen("https://www.boxofficemojo.com" + link)
		html = response.read()
		f.write(html)
		f.close()
		os.rename("deep_link_movie_html/" + filename + ".html.temp","deep_link_movie_html/" + filename + ".html")
		time.sleep(1)

	


