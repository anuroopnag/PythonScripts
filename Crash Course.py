#!/usr/bin/env python
# coding: utf-8

# In[11]:


s=('user@domain.com')
print(s.split('@'))


# In[12]:


def domainGet(dom):
    return dom.split('@')[1]
domainGet('user@domain.com')


# In[16]:


s1="hi iam here"
if 'hi' in s1:
    print("true")


# In[ ]:


def findDog(string):
    if 'dog' in string:
        return True
    elif 'Dog' in string:
        return True
    else:
        print('Sorry no dog here')


# In[17]:


s2="dog is here"
for val in s2:
    print (val)


# In[23]:


def countDog(string):
    lst=(string.split())
    count=0
    for val in lst:
        if val=='dog':
            count = count+1
    return count
countDog('This dog runs faster than the other dog dude!')


# In[27]:


seq = ['soup','dog','salad','cat','great']
#print(seq[0])
for val in seq:
    print(val[0])
    


# In[28]:


seq = ['soup','dog','salad','cat','great']
list(filter(lambda var: var[0]=='s',seq))


# In[29]:


def caught_speeding(speed, is_birthday):
    if speed>=60 and speed<=65 and is_birthday==True:
        print("No ticket")
    elif speed<=60 and is_birthday==False:
        print("No ticket")
    elif speed>=66 and speed<=85 and is_birthday==True:
        print("Small Ticket")
    elif speed>=61 and speed<=80 and is_birthday==False:
        print("Small Ticket")
    elif speed>= 81 and speed<=86 and is_birthday==True:
        print("Big Ticket")
    elif speed>=81 and is_birthday==False:
        print("Big Ticket")
caught_speeding(81,True)
caught_speeding(81,False)

