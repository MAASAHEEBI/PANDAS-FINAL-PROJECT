#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Pandas assignment 2


# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# 1)importing dataset from url

url='https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv'
df=pd.read_csv(url)
df


# In[3]:


# 2)High level data ubderstanding

#no of rows
df.shape[0]


# In[4]:


#no of columns
df.shape[1]


# In[5]:


df.dtypes


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


# 3) low level data understanding
#count of unique values in location column
df['location'].nunique()

df


# In[9]:


#which content has maximum frequency using values
df.max()


# In[10]:


#find max and mean value in total_cases
df['total_cases'].max()


# In[11]:


df['total_cases'].mean()


# In[12]:


df['total_deaths'].describe()


# In[13]:


#which content has max human developement
max_human_dev=df.human_development_index .max()
set(df.loc[df.human_development_index ==max_human_dev,'continent'])


# In[14]:


#which content has min gdb per capita
min_gdp=df.gdp_per_capita.min()
set(df.loc[df.gdp_per_capita==min_gdp,'continent'])


# In[15]:


#filter dataframe with 
df=pd.read_csv(url,usecols=["continent","location","date","total_cases","total_deaths","gdp_per_capita","human_development_index"])
df


# In[18]:


df.drop_duplicates()


# In[19]:





df.isna().sum()


# In[20]:


(646/57394)*100


# In[21]:


df=df[df['continent'].notna()]
df.reset_index(inplace=True,drop=True)
df


# In[22]:


3636/56748


# In[23]:


df=df[df['total_cases'].notna()]
df.reset_index(inplace=True,drop=True)
df


# In[24]:


df['total_deaths']=df['total_deaths'].fillna(0)
df


# In[25]:


df['gdp_per_capita'].fillna(0,inplace=True)
df


# In[26]:


df['human_development_index'].fillna(0,inplace=True)
df


# In[27]:


df.isna().sum()


# In[28]:


#6)Convert Date format to datetime format
df['date']=pd.to_datetime(df['date'])


# In[29]:


df


# In[30]:


#6b)create a new column month
df['month']=df['date'].dt.month


# In[31]:


#7)find max value in all columns using group by 'continent'
df_groupby=df.groupby(['continent']).max()
df_groupby


# In[32]:


#b) reset index
df_groupby.reset_index(level=['continent'],inplace=True)


# In[35]:


df_groupby


# In[34]:


df_groupby['total_deaths_to_total_cases']=(df_groupby['total_deaths']/df_groupby['total_cases'])


# In[36]:


#9)Data Visualization
#gdp_per_capita income by using histogram
import seaborn as sns


# In[37]:


sns.histplot(df_groupby['gdp_per_capita'])


# In[40]:


#9b Scatter plot of total_cases and gdp_per_capita
sns.scatterplot(data=df_groupby,x='total_cases',y='gdp_per_capita')


# In[41]:


#9c pairplot on df_groupby dataset
sns.pairplot(df_groupby)


# In[42]:


#9d plot a bar plot using continent with total cases
sns.catplot(x='continent',y='total_cases',kind='bar',data=df_groupby)


# In[43]:


#10) Save df_groupby in your local drive using panda.to_csv function.
df_groupby.to_csv('df_groupby.csv',index=False)


# In[ ]:




