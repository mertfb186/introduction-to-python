#!/usr/bin/env python
# coding: utf-8

# In[2]:


mylist = [3,4,5,6,7,8]
print(mylist[3:]+mylist[:3])


# In[3]:


x=int(input("Tek basamaklı bir tamsayı giriniz:"))
if (0<=x<10):
    print(list(range(0,x+1,2)))
else:
    print("Yanlış Girdiniz!!Lütfen tek basamaklı bir tamsayı giriniz")

