# -*- coding: utf-8 -*-
"""Task-6 Main flow services and technologies

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1560uYYSiTYzbC9Wnk5C9Z2kCpXWlV0Tz

Description:
The project involved selecting a dataset of interest and performing a
comprehensive analysis to extract meaningful insights. The project
required applying a full data science workflow, including data cleaning,
exploratory data analysis (EDA), question formulation, and data
visualization.

RESPONSIBILITY:
1. Data Cleaning: Handled missing data, outliers, and inconsistencies to
ensure the dataset was suitable for analysis.

2. Exploratory Data Analysis (EDA): Performed EDA to understand the
distribution of data, relationships between variables.

3. Question Formulation: Developed specific minimum 7 questions related
to disney_plus titles, and solve each question by using appropriate
functions.

4. Data Visualization: Created visualizations using tools like Matplotlib,
Seaborn, to effectively present the findings and insights gained from the
analysis. This included charts, graphs, and other visual aids to make the
results easy to understand.

importing necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""loading dataset"""

df = pd.read_csv('/content/disney_plus_titles.csv')

df.head()

df.info()

"""data cleaning
handling missing values
"""

df.isnull().sum()

del df['description']

df['director'] = df['director'].fillna('unknown')

df['cast'] =  df['cast'].fillna('unknown')

df['country']= df['country'].fillna('notspecified')

df = df.dropna(subset=['date_added','rating'])

df.isnull().sum()

df['date_added'] = pd.to_datetime(df['date_added'])

df['month_added'] = df['date_added'].dt.month

df['year_added'] = df['date_added'].dt.year

"""exploratory data analysis"""

df['type'].value_counts()

df['release_year'].describe()

df['country'].value_counts().head()

df['rating'].value_counts()

plt.figure(figsize=(8, 5))
sns.heatmap(df[['release_year', 'month_added', 'year_added']].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#What are the most common genres on Disney Plus?
all_genres = df['listed_in'].dropna().str.split(',', expand=True).stack()
genre_counts = all_genres.value_counts()
top_10_genres = genre_counts.head(10)
plt.figure(figsize=(10, 6))  # Set the size of the plot
top_10_genres.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'lightcoral', 'plum', 'gold', 'lightyellow', 'lightpink', 'beige', 'lavender'])
plt.title("Top 10 Most Common Genres on Disney Plus", fontsize=14)
plt.xlabel("Genres", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

#How does the distribution of movies compare to TV shows?
type_counts = df['type'].value_counts()
plt.figure(figsize=(8,5))
type_counts.plot(kind ='bar', color= ['skyblue','lightgreen'])
plt.title("Distribution of Movies vs TV Shows on Disney Plus", fontsize=14)
plt.xlabel("Type",fontsize = 12)
plt.ylabel("count",fontsize = 12)
plt.show()

#What is the trend in the number of titles added annually?
titles_per_year = df['year_added'].value_counts().sort_index()
plt.figure(figsize=(8, 6))
titles_per_year.plot(kind='line', marker='o', color='coral')
plt.title("Trend in Number of Titles Added Annually to Disney Plus", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Number of Titles Added", fontsize=12)
plt.show()

#Which country contributes the most content?
country_counts = df['country'].value_counts()
most_content_country= country_counts.idxmax()
most_content_count = country_counts.max()
plt.figure(figsize=(10,6))
country_counts.head(10).plot(kind = 'bar',color = 'lightblue')
plt.title("Top 10 Countries Contributing the Most Content on Disney Plus", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)
print(f"The country with the most content is: {most_content_country} with {most_content_count} titles.")
plt.show()

#Which directors have directed the highest number of titles?
director_counts = df['director'].value_counts()
top_10_directors = director_counts.head(10)
plt.figure(figsize=(10, 6))
top_10_directors.plot(kind='bar', color='salmon')
plt.title("Top 10 Directors with the Highest Number of Titles", fontsize=14)
plt.xlabel("Director", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)
plt.show()
print("Top 10 Directors with the Highest Number of Titles:")
print(top_10_directors)

#How many movies and TV shows have been added to Disney Plus each year?
titles_by_year = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)
plt.figure(figsize=(100, 6))
titles_by_year.plot(kind='bar', stacked=True, color=['skyblue', 'orange'], figsize=(12,6))
plt.title('Number of Movies and TV Shows Added to Disney Plus Each Year', fontsize=14)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Titles Added', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Type', labels=['Movies', 'TV Shows'])
plt.tight_layout()
plt.show()

# Which title has the most actors or cast members?
df['cast_count'] = df['cast'].str.split(',').apply(len)
max_cast_title = df.loc[df['cast_count'].idxmax()]
print(f"The title with the most actors is: {max_cast_title['title']}")
print(f"Number of actors: {max_cast_title['cast_count']}")
top_10_cast = df[['title', 'cast_count']].nlargest(10, 'cast_count')
plt.figure(figsize=(10, 6))
plt.barh(top_10_cast['title'], top_10_cast['cast_count'], color='skyblue')
plt.xlabel('Number of Actors')
plt.title('Top 10 Titles with the Most Actors on Disney Plus')
plt.show()