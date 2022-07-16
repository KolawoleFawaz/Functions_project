#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maximum(a,b,c):
    numbers = [a,b,c]
    largest_number = numbers[0]
    
    for number in numbers:
        if number > largest_number:
            largest_number = number
    return largest_number


# In[2]:


maximum(20,35,19)


# In[ ]:




