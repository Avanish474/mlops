#!/usr/bin/env python
# coding: utf-8

# In[51]:


import tensorflow as tf
from tensorflow import keras
import os
# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
n=2
previous = 2
new = 2**n
accuracy_file=open('/tf/tensorflow-tutorials/accuracy.txt','rt')
while((int(accuracy_file.read(5))*100)<80):
    
    f=open('/tf/tensorflow-tutorials/classifications.py','rt')
    data=f.read()   
      data=data.replace('n={0}'.format(previous),'n={0}'.format(new))            
    f.close()
    f=open('/tf/tensorflow-tutorials/classifications.py','wt')
   
    f.write(data)
    f.close()
    os.system('python3 /tf/tensorflow-tutorials/classifications.py')
    accuracy_file=file
    previous=new
    n=2*n
    new=2**n
    


# In[ ]:


    new=2**n
    
exit()

# In[ ]:




