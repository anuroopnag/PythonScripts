#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install matplotlib


# In[7]:


import matplotlib.pyplot as plt
from random import sample
data = sample(range(1, 1000), 100)
data
plt.hist(data)


# In[9]:


import numpy as np
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
data


# In[11]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
x,y,z


# In[15]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Title')


# In[17]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,y,'r-')
ax2.plot(x,y,'r--')


# In[23]:


fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
ax1.plot(x,z,'r-')
ax2.plot(x,y,'r--')
ax2.set_xlim(20.0,22.0)
ax2.set_ylim(30,50)
ax2.set_title('Zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('z')
ax1.set_xlabel('x')
ax1.set_ylabel('y')


# In[14]:


fig,ax = plt.subplots(1,2)
ax[0].plot(x,y,'r',lw=1,marker='o')
ax[1].plot(x,z,'r--',lw=5)


# In[25]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
fig,ax = plt.subplots(1,2,figsize=(12,2))
ax[0].plot(x,y,'r',lw=1,ls='-',marker='*')
ax[1].plot(x,z,'r--',lw=1,marker='o')

