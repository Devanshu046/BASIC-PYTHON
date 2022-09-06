#!/usr/bin/env python
# coding: utf-8

# In[5]:


for latter in 'shivam':
    print("name:",latter)
    
name=['hi','xyz']
for item in name :
    print(item)


# In[11]:


for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print(i,j,num)
            break
else:
     print(num,'yes prime no')
    


# In[18]:


num=int(input("enter no :"))
print(num)
from math import pi
s=pi*num
print(s)


# In[15]:


age=int(input("enter age "))
print(f"my age is {age}")


# In[16]:


from math import pi
s=pi*12
print(s)


# In[22]:


var1=201250107048
var2="shivam"
print(var1 , var2)


# In[26]:


var1=201250107048
var2="shivam"
print(var1 , var2)
print(type(var1))
print(type(var2))


# In[30]:


str="  shivam"
str1="  hi"
print(str + str1)
print(type(str + str1))


# In[32]:


name="shivam"
print(name)
print(len(name))


# In[34]:


name="shivam"

print(len(name))
name[:3]


# In[35]:


name="shivam"
print(name)
print(len(name))
name[-6:]


# In[36]:


#tuple
tup1=("shivam",20,"parmar")
print(tup1)
print(type(tup1))


# In[37]:


tup1=("shivam",20,"parmar")
print(tup1)
tup1[1:4]


# In[42]:


tup1=("shivam",20,"parmar")
tup2=("Devanshu",20,"parmar")
print(tup1+tup2)


# In[52]:


#list
list1=["shivam",20,100]
print(list1)
print(type(list1))
print(len(list1))
list1[0:1]
list1.remove(20)
print(list1)


# In[56]:


#dictionary
tup1={1:"shivam",2:20,3:"parmar"}
print(tup1)
print(tup1.keys())
print(tup1.values())


# In[ ]:




