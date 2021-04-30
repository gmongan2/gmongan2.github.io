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


# In[5]:


df['price'].mean()


# In[6]:


df.describe


# In[7]:


ztest_result = ztest(df['price'], value=27057.16763)



z_score, p_value = ztest_result
ztest_result


# In[8]:


from scipy.stats import bayes_mvs
cartier_95 = bayes_mvs(df['price'],(.8))


cartier_95[0]


# In[9]:


df['percent_of_my_money'] = df['price']/ 2500
df


# In[10]:


ztest_result = ztest(df['percent_of_my_money'], value=1.0)



z_score, p_value = ztest_result
ztest_result


# In[11]:


percent_money95 = bayes_mvs(df['percent_of_my_money'],(.95))


percent_money95[0]


# In[12]:


df_or=pd.read_csv('cartier_catalog-csv.csv')
df_or


# In[17]:


df_or['price'].hist(density= True)


# In[18]:


df_or['price'].mean()


# In[19]:


df_or.describe


# In[25]:


ztest_result = ztest(df_or['price'], value=27057.16763)



z_score, p_value = ztest_result
ztest_result


# In[26]:


from scipy.stats import bayes_mvs
cartier_95 = bayes_mvs(df_or['price'],(.8))


cartier_95[0]


# In[27]:


df_or['percent_of_my_money'] = df_or['price']/ 2500
df_or


# In[28]:


ztest_result = ztest(df_or['percent_of_my_money'], value=1.0)



z_score, p_value = ztest_result
ztest_result


# In[29]:


percent_money95 = bayes_mvs(df_or['percent_of_my_money'],(.95))


percent_money95[0]


# In[ ]:




