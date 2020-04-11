CONTENTS OF THIS FILE
---------------------
* Developer: Jaeyoung Kim
* Status of this document.
This document is a submission to ECON 8070 Class. 
Comments on this document should be sent to jaeyouk@clemson.edu.

 * Introduction
 This document defines a profile of my web scraping project for bwebsite office movie data from https://www.boxofficemojo.com/. 

 * Summary of files

	(1) boxoffice_request_links.py
	(2) boxoffice_parse_links.py
	(3) boxoffice_request_deeplink.py
	(4) boxoffice_parse_deeplink.py
	(5) boxoffice_request_deeplink_movie.py
	(6) boxoffice_parse_deeplink_movie.py
	(7) boxoffice_merge.py

	Sequence of the steps follows the sequence of the above files. 

 * Usage

	(1) boxoffice_request_links.py: Collect the html files of daily box office data on yearly webpage: https://www.boxofficemojo.com/daily/"target_year"/?view=year. "target_year" can be specified in the code by changing the array of years. The defalt years are "2017", "2016", "2005", "2004", "1994", "1993", "1992". The html files are stored in a folder naemd 'html_files' that is created in the same work directory of python file. 

		Example:
		years = ["2017", "2016", "2005", "2004", "1994", "1993", "1992"]

	(2) boxoffice_parse_links.py: Parse the links of daily box office data from yearly webpage: https://www.boxofficemojo.com/daily/"target_year"/?view=year and save them to a CSV file, named 'boxoffice_links.csv', for the use of the next steps. 

	(3) boxoffice_request_deeplink.py: Collect the html files of daily box office data on daily webpage. The html files are stored in a folder naemd 'deep_link_html' that is created in the same work directory of python file. 

	(4) boxoffice_parse_deeplink.py: Parse the daily data of each day and save them to a CSV file including the movie name, daily gross box office, number of theaters, gross box office to date, number of days in release, distributers along with the links for website of that movie, and save them to a CSV file. The CSV file is named 'movie_deeplinks.csv'. 

	(5) boxoffice_request_deeplink_movie.py: Collect the html files of unique movie data on each movie webpage. 
	The html files are stored in a folder naemd 'deep_link_movie_html' that is created in the same work directory of python file. 

	(6) boxoffice_parse_deeplink_movie.py: parse the data of opening money, release date, MPAA, running time(in hour as the unit, e.g., 2 h 30 min = 2.5h), Genres, in release period(use days as the unit), widest release, the ID of IMDbPro, and save them to a CSV file. The CSV file is named 'movie_web_deeplinks.csv'.
	Note that Some data including MPAA, Genres, and etc. are missing, you they are recorded as N/A (Not Available). 

	(7) boxoffice_merge.py: Merge the two datasets into a dataset with each movie's characteristics and daily box office for specified years. In particular, the two data sets are 'movie_deeplinks.csv' (the daily box office data of each movie) from step (4) and 'movie_web_deeplinks.csv' (the data of each movie's characteristics) from step (6). The merged dataset is saved to a CSV file named 'merged_data.csv'.

	The resulting dataset contains 'Date', 'daily box office', 'distributor', 'gross box office to date','movie name', 'number of days in release', 'theaters', 'IMDB ID', 'MPAA', 'genres', 'in release', 'opening', 'release date', 'running time', 'widest release'.

 * TODO 
 None

 * Troubleshooting
 Questions can be sent to jaeyouk@clemson.edu.
