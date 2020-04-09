import pandas as pd
import numpy as np

daily_boxoffice = pd.read_csv("parsed_files/movie_deeplinks.csv",
                         keep_default_na=False, na_values=[""])


movie_data = pd.read_csv("parsed_files/movie_web_deeplinks.csv",
                         keep_default_na=False, na_values=[""])


# Read in first 10 lines of surveys table
daily_boxoffice_sub = daily_boxoffice.head(10)
# Grab the last 10 rows
daily_boxoffice_sub_last10 = daily_boxoffice.tail(10)
# Reset the index values to the second dataframe appends properly
daily_boxoffice_sub_last10 = daily_boxoffice_sub_last10.reset_index(drop=True)
# drop=True option avoids adding new index column with old index values

movie_data_sub = pd.read_csv("parsed_files/movie_web_deeplinks.csv",
                         keep_default_na=False, na_values=[""])
# print(movie_data_sub)
# print(daily_boxoffice_sub)

movie_data_sub.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
movie_data_sub.drop(["a"], axis=1, inplace=True)

daily_boxoffice_sub.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
daily_boxoffice_sub.drop(["a"], axis=1, inplace=True)

print(movie_data_sub)
print(daily_boxoffice_sub)

boxoffice_index = daily_boxoffice_sub.columns
print(boxoffice_index)
movie_index = movie_data_sub.columns
print(movie_index)

merged_data = pd.merge(daily_boxoffice, movie_data, on='movie name')

merged_data.rename({"Unnamed: 0_x":"a"}, axis="columns", inplace=True)
merged_data.drop(["a"], axis=1, inplace=True)
merged_data.rename({"Unnamed: 0_y":"a"}, axis="columns", inplace=True)
merged_data.drop(["a"], axis=1, inplace=True)
merged_data.rename({"movie_links ":"a"}, axis="columns", inplace=True)
merged_data.drop(["a"], axis=1, inplace=True)
print(merged_data)

merged_index = merged_data.columns
print(merged_index)
df = merged_data

df.to_csv(r"parsed_files/merged_data.csv")
