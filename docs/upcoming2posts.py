
# coding: utf-8

# # upcoming2posts
# 
# By Stuart Geiger (@staeiou), MIT license
# 
# This is a script you run the day after THW, which changes yesterday's file from "upcoming" to "posts" so that the next week's topic shows on the main page.

# In[78]:


# In[1]:

import datetime
from datetime import timedelta
import os
import glob
import re


# In[ ]:




# In[2]:

today = datetime.date.today()
yesterday = today - timedelta(1)


# In[3]:

if yesterday.isoweekday() == 2:
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    


# In[4]:

filename = glob.glob("_posts/" + yesterday_str + "*")[0]


# In[5]:

with open(filename, "r") as file:
    file_text = file.read()
file_text


# In[6]:

file_text = file_text.replace('category: upcoming', 'category: posts')
file_text = file_text.replace('category:upcoming', 'category: posts')
file_text


# In[7]:

with open(filename, "w") as file:
    file.write(file_text)




