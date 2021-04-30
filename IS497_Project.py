#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
get_ipython().system('conda install --yes --prefix {sys.prefix} numpy')


# In[2]:


get_ipython().system('pip install pandas')
import pandas as pd
from statsmodels.stats.weightstats import ztest
from scipy.stats import norm
from scipy import stats
import numpy as np


# In[3]:


df=pd.read_csv('cartier_catalog.csv')
df


# In[4]:


df['price'].hist(density= True)


# In[6]:


original_mean = df['price'].mean()
original_mean


# In[7]:


df.describe


# In[8]:


ztest_result = ztest(df['price'], value=27057.16763)



z_score, p_value = ztest_result
ztest_result


# In[9]:


from scipy.stats import bayes_mvs
cartier_95 = bayes_mvs(df['price'],(.8))


cartier_95[0]


# In[10]:


df['percent_of_my_money'] = df['price']/ 2500
df


# In[11]:


ztest_result = ztest(df['percent_of_my_money'], value=1.0)



z_score, p_value = ztest_result
ztest_result


# In[12]:


percent_money95 = bayes_mvs(df['percent_of_my_money'],(.95))


percent_money95[0]


# In[13]:


df_or=pd.read_csv('cartier_catalog-csv.csv')
df_or


# In[14]:


df_or['price'].hist(density= True)


# In[31]:


cleaned_mean= df_or['price'].mean()
cleaned_mean


# In[16]:


df_or.describe


# In[17]:


ztest_result = ztest(df_or['price'], value=27057.16763)



z_score, p_value = ztest_result
ztest_result


# In[18]:


from scipy.stats import bayes_mvs
cartier_95 = bayes_mvs(df_or['price'],(.8))


cartier_95[0]


# In[19]:


df_or['percent_of_my_money'] = df_or['price']/ 2500
df_or


# In[20]:


ztest_result = ztest(df_or['percent_of_my_money'], value=1.0)



z_score, p_value = ztest_result
ztest_result


# In[21]:


percent_money95 = bayes_mvs(df_or['percent_of_my_money'],(.95))


percent_money95[0]


# In[32]:


if original_mean > cleaned_mean:
    print("I can afford most of it")
else: 
    print("I am poor")


# In[ ]:




