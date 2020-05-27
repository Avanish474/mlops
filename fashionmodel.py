import os


while((float(open('/tf/tensorflow-tutorials/accuracy.txt','rt').read(5))*100)<=89):
    n=int(open('/tf/tensorflow-tutorials/n.txt','rt').read())
    f=open('/tf/tensorflow-tutorials/classifications.py','rt')
    data=f.read()   
    data=data.replace('n={0}'.format(n),'n={0}'.format(n*2))            
    f.close()
    f=open('/tf/tensorflow-tutorials/classifications.py','wt')
    f.write(data)
    f.close()
    os.system('python3 /tf/tensorflow-tutorials/classifications.py')

# In[ ]:
    
exit()

# In[ ]:




