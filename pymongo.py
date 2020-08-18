#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pymongo
from pymongo import MongoClient
mflix=MongoClient("mongodb+srv://m220student:m220password@mflix.qhpd1.mongodb.net/sample_mflix?retryWrites=true&w=majority")
mydb=mflix["sample_mflix"]
for coll in mydb.list_collection_names():
    print(coll)


# In[ ]:




