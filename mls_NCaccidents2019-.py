#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set(font_scale=1.5)

nc_df = pd.read_csv("Resources/NC-Accidents.csv")
nc_df.head()


# In[4]:


nc_df


# In[13]:


nc_df.figure(figsize=(14,8)) # set the size of the graph
_ = sns.regplot(data=df, x= 'Source', y='Severity')


# In[8]:


nc_df.describe


# In[14]:


# create tabular correlation matrix
corr = nc_df.corr()
_, ax = plt.subplots(figsize=(13,10)) 

# graph correlation matrix
_ = sns.heatmap(corr, ax=ax,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values,
                cmap='coolwarm')


# In[ ]:





# In[ ]:




