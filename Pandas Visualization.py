#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
df3 = pd.read_csv("df3")
df3.head()


# In[2]:


df3.plot.scatter(x='b',y='a',c='r',s=100,figsize=(12,3))


# In[3]:


df3['a'].plot.hist()


# In[4]:


plt.style.use('ggplot')
df3['a'].plot.hist(bins=20,alpha=0.5)


# In[11]:


df3[['a','b']].plot.box()


# In[16]:


df3['d'].plot.kde()


# In[18]:


df3['d'].plot.kde(lw=5,ls='--')


# In[26]:


df3.iloc[0:30].plot.area(alpha=0.5)


# In[44]:


df3.iloc[0:30].plot.area(alpha=0.5)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


# In[ ]:


plt.legend()

