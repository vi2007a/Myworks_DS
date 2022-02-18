#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df_used_cars = pd.read_csv("bar_chart_data.csv")


# In[4]:


df_used_cars


# In[5]:


plt.bar(x = df_used_cars["Brand"],
           height = df_used_cars["Cars Listings"])
plt.show()


# In[7]:


plt.figure(figsize = (9 , 6))
plt.bar(x = df_used_cars["Brand"],
           height = df_used_cars["Cars Listings"])
plt.show()


# In[11]:


plt.figure(figsize = (9 , 6))
plt.bar(x = df_used_cars["Brand"],
           height = df_used_cars["Cars Listings"])
plt.xticks(rotation = 45)
plt.show()


# In[12]:


import seaborn as sns
sns.set()


# In[13]:


plt.figure(figsize = (9 , 6))
plt.bar(x = df_used_cars["Brand"],
           height = df_used_cars["Cars Listings"])
plt.xticks(rotation = 45)
plt.show()


# In[ ]:




