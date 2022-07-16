#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def equ():
    numbers = input("Provide D: ")
    numbers = numbers.split(',')
    
    output_result = []
    C = 50
    H = 30
    for D in numbers:
        Q = round(math.sqrt(2 * C * int(D) / H))
        output_result.append(Q)

    return print(output_result)


equ()


# In[ ]:




