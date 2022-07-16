#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def equ():
    numbers = input("Provide D: ")
    numbers = numbers.split(',')
    
    output_result = []
    for D in numbers:
        equation = round(math.sqrt(2 * 50 * int(D) / 30))
        output_result.append(equation)

    return print(output_result)


equ()


# In[ ]:




