# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello World")
print("Pangi is good")
import pandas as pd

movies =pd.read_csv("C:/Users/ccm/Downloads/movie_dataset.csv")
print(movies)

movies = pd.read_csv("C:/Users/ccm/Downloads/movie_dataset.csv")
pd.set_option('display.max_columns',None)
print(movies.describe())

# Cleaning the dataset
movies.rename(columns={"Runtime (Minutes)": "Runtime_Minutes", "Revenue (Millions)": "Revenue_Millions"}, inplace=True)

movies
movies.isna().sum()

movies_dropped_na = movies.dropna()
print(movies_dropped_na)
movies_dropped_na.isna().sum()

#Q1
print(movies_dropped_na['Rating'].max())
print(movies_dropped_na.query('Rating==9')['Title'])
#Q2
print(movies_dropped_na["Revenue_Millions"].mean())
#Q3
print(movies_dropped_na['Year'].unique())
values = [2015, 2016]
movies_dropped_na_and_yrs = movies_dropped_na[movies_dropped_na.Year.isin(values) == True]
print(movies_dropped_na_and_yrs['Year'].unique())
ave_revenue_2015_2017 = movies_dropped_na_and_yrs["Revenue_Millions"].mean()
print(ave_revenue_2015_2017)
#Q4
values.remove(2015)
print(values)
movies_2016 = movies_dropped_na[movies_dropped_na.Year.isin(values) == True]

print(movies_2016['Year'].unique())

len(movies_2016)
movies_2016 = movies[movies.Year.isin(values) == True]

print(movies_2016['Year'].unique())
len(movies_2016)

#Q5
CN_directed = movies_dropped_na[movies_dropped_na['Director'] == 'Christopher Nolan']
len(CN_directed)

#Q6
Eight_rating_more = movies_dropped_na[movies_dropped_na['Rating'] >= 8.0]
len(Eight_rating_more)
Eight_rating_more = movies[movies['Rating'] >= 8.0]
len(Eight_rating_more)

#Q7 
print(CN_directed)
print(CN_directed['Rating'].median())

#Q8 
grpd_rating = movies_dropped_na.groupby(['Year'],as_index=False).Rating.mean()
print(grpd_rating)

grpd_rating = movies.groupby(['Year'],as_index=False).Rating.mean()
print(grpd_rating)

#Q9
print(len(movies_dropped_na))
movies_sum_pyr = movies_dropped_na.groupby(['Year'],as_index=False).Rank.count()
print(movies_sum_pyr)

amt_inc = 198 - 41
print(amt_inc)
per_inc = 157 / 41 * 100
print(per_inc)

per_inc_ = 253 / 44 * 100
print(per_inc_)

print(len(movies))

movies_sum_pyr_na = movies.groupby(['Year'],as_index=False).Rank.count()
print(movies_sum_pyr_na)

amt_inc_ = 297 - 44
print(amt_inc_) # 253 inc
per_inc_ = 253 / 44 * 100
print(per_inc_)

#Q10
Actors = movies_dropped_na[['Actors']].copy()
print(Actors)

Actors['Actors'] = Actors['Actors'].str.split(',')
Actors = Actors.explode('Actors')
print(Actors)

Actors['count'] = 1
grouped = Actors.groupby('Actors')

Actors_feat_count = grouped['count'].count()
print(Actors_feat_count.info())

#Q11
Genres = movies_dropped_na[['Genre']].copy()
print(Genres)
Genres['Genre'] = Genres['Genre'].str.split(',')

Genres = Genres.explode('Genre')
print(Genres)

Genres_unique = Genres.drop_duplicates()
print(len(Genres_unique))

#Q12
corr = movies_dropped_na.corr(method = 'pearson')
print(corr)


