#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install seaborn


# In[12]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
titanic.head()


# In[3]:


sns.jointplot(x='fare',y='age',data=titanic)


# In[4]:


sns.distplot(titanic['fare'],kde=False,color='red',bins=30)


# In[5]:


sns.boxplot(x='class',y='age',data=titanic)


# In[6]:


sns.swarmplot(x='class',y='age',data=titanic)


# In[7]:


sns.countplot(x='sex',data=titanic)


# In[8]:


tc = titanic.corr()
sns.heatmap(tc,cmap='coolwarm')


# In[9]:


g=sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')


# In[11]:


g=sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')

