#!/usr/bin/env python
# coding: utf-8

# In[4]:


def hyph(lists):
    n = lists.split("-")
    n.sort()
    result = "-".join(n)
    return print(result)


# In[5]:


hyph("green-red-yellow-black-white")


# In[ ]:




