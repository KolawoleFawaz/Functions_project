#!/usr/bin/env python
# coding: utf-8

# In[13]:


def sums(add,odd_addition):
    number = 0
    nom = 0
    for x in add:
        number += x
    for y in range(len(odd_addition)):
        if y % 2 == 0:
            nom += odd_addition[y]
    return number,nom


# In[17]:



def multiplies(my_nums,even_mult):
    num = 1
    nom = 1
    for a in my_nums:
        num *= a
    for b in range(len(even_mult)):
        if not b % 2 == 0:
            nom *= even_mult[b]
    return num,nom


# In[15]:


sums([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])


# In[18]:


multiplies([1,2,3,4,5,6],[1,2,3,4,5,6])


# In[ ]:




