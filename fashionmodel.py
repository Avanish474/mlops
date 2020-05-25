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

os.system('ls saved_model')
os.system('ls saved_model/my_model1')
new_model=tf.keras.models.load_model('saved_model/my_model1')
new_model.summary()
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images = train_images / 255.0
test_images = test_images / 255.0
loss,acc=new_model.evaluate(test_images,  test_labels, verbose=2)
print('Restored model,accuracy: {:5.2f}%'.format(100*acc))
print(new_model.predict(test_images).shape)
while acc<80:    
    f=open('/tf/tensorflow-tutorials/classifications.py','rt')
    data=f.read()
    data=data.replace('n={0}'.format(previous),'n={0}'.format(new))  
    f.close()
    f=open('/tf/tensorflow-tutorials/classifications.py','wt')
    f.write(data)
    f.close()
    os.system('python3 /tf/tensorflow-tutorials/classifications.py')
    previous=new
    n=2*n
    new=2**n
    
exit()

# In[ ]:




