import pandas as pd
import numpy as np

daily_boxoffice = pd.read_csv("movie_deeplinks.csv",
                         keep_default_na=False, na_values=[""])


movie_data = pd.read_csv("movie_web_deeplinks.csv",
                         keep_default_na=False, na_values=[""])
# Read in first 10 lines of surveys table
daily_boxoffice_sub = daily_boxoffice.head(10)
# Grab the last 10 rows
daily_boxoffice_sub_last10 = daily_boxoffice.tail(10)
# Reset the index values to the second dataframe appends properly
daily_boxoffice_sub_last10 = daily_boxoffice_sub_last10.reset_index(drop=True)
# drop=True option avoids adding new index column with old index values