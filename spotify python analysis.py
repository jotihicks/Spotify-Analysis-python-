#!/usr/bin/env python
# coding: utf-8

# In[158]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:





# In[100]:


get_ipython().system('pip install pandas')


# In[101]:


import pandas as pd


# In[72]:


df_tracks = pd.read_csv('C:/Users/HP/Desktop/data analysis files/tracks.csv')
df_tracks.head()


# In[48]:


# null values

pd.isnull(df_tracks).sum()


# In[49]:


df_tracks.info()


# In[58]:


sorted_df = df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df


# In[51]:


df_tracks.describe().transpose()


# most_popular = df_tracks.query('popularity>90' inplace = false).sort_values('popularity', ascending = false)
# most_popular[:10]

# In[61]:


most_popular = df_tracks.query('popularity>90', inplace = False).sort_values('popularity', ascending = False) 
most_popular[:10]


# In[ ]:





# In[73]:


df_tracks.set_index("release_date", inplace=True)
df_tracks.indexed=pd.to_datetime(df_tracks.index)
df_tracks.head()


# In[77]:


df_tracks[["artists"]].iloc[18]


# In[184]:


df_tracks["duration"]= df_tracks['duration'].apply(lambda x: round(x/1000))
df_tracks.drop('duration', inplace=True, axis=1)


# In[180]:


df_tracks.duration.head()


# In[91]:


corr_df=df_tracks.drop(["key","mode","explicit"],axis=1).corr(method="pearson")
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True,fmt=".1g", vmin=-1, vmax=1, center=0, cmap="summer", linewidths=1, linecolor="Black")
heatmap.set_title("Correlation Heatmap Between Variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=90)


# In[118]:


sample_df = df_tracks.sample(int(0.004*len(df_tracks)))


# In[119]:


print(len(sample_df))


# In[131]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y= "loudness", x = "energy", color = "y").set(title = "Loudness vs Energy Correlation")


# In[137]:


plt.figure(figsize=(10,6))
sns.regplot(data = sample_df, y = "popularity", x = "acousticness", color = 'r').set(title = "Popularity vs Acousticness Correlation")


# In[151]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year


# In[152]:


#pip install --user seaborn==0.11.0


# In[153]:


sns.displot(years,discrete=True,aspect=2,height=5 ,kind="hist").set(title="Number of songs per year")


# In[164]:


total_dr = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title="Year vs Duration")
plt.xticks(rotation=90)


# In[165]:


total_dr=df_tracks.duration
sns.set_style(style="whitegrid")
fig_dims = (10, 5)
fig, ax = plt.subplots(figsize=fig_dims)
fig=sns.lineplot(x=years, y=total_dr,ax=ax).set(title="Year vs Duration")
plt.xticks(rotation=60)


# In[173]:


df_genre=pd.read_csv("C:/Users/HP/Desktop/data analysis files/SpotifyFeatures.csv")


# In[174]:


df_genre.head()


# In[175]:


plt.title("Duration of the Songs In Different Genres")
sns.color_palette("rocket", as_cmap= True)
sns.barplot(y='genre', x='duration_ms', data=df_genre)
plt.xlabel("Duration in milli seconds")
plt.ylabel("Genres")


# In[177]:


sns.set_style(style = 'darkgrid')
plt.figure(figsize=(10,5))
famous = df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y='genre', x='popularity', data = famous).set(title= "Top 5 Genres by Popularity")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




