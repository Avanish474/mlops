# mlops

# Have you been thinking to add automation to your machine learning project ? Well here is a way you can make it happen!

# Prerequisites 

1) Concepts of redhat operating system commands

2) Basic concepts of Docker 

3) Basics of Git and Github

4) Basics of Jenkins

#  Note : All above prerequisites should be clear to you if you wanna proceed further .Setup the softwares listed above in you pc or laptop



![Image description](https://github.com/Avanish474/mlops/blob/93f527b538aea168849ce0dcba94b8509212cb67/mld.jpg)



# Task to perform

1. Create container image that has Python3 and Keras or numpy installed using dockerfile

2. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins

3. Job1 : Pull the Github repo automatically when some developers push repo to Github.

4. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

5. Job3 : Train your model and predict accuracy or metrics.

6. Job4 : if metrics accuracy is less than 80% , then tweak the machine learning model architecture and retrain it.

7. Job5: Notify that the best model is being created

8. Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left


# Solution to above task and setup

1) Create a directory inside your home directory of redhat:
 
 
   mkdir /project
 
 
   Go inside this directory:
 
 
   cd /project
 
 
   Create an container image having python3 ,keras and numpy previously installed using Dockerfile.For doing this refer to this file :
  
   
    https://github.com/Avanish474/mlops/blob/master/Dockerfile
  
  
   and then type 
  
  
   docker build -t riseweb:v1
  
  
   where riseweb:v1 is your image name
   
   
 
 2) After doing the above job now you can start your container and launch jupyter notebook by the following command:
 
 
 docker run -it --rm -v $(realpath ~/notebook):/tf/notebooks -p 8888:8888 --name fashion riseweb:v1
 
 
 You'll get a link to open jupyter notebook to do your further tasks
 
 
 3) Create a new file in jupyter notebook and type your machine learning code .For refernce you can get an idea clicking on this link of my sample codes :
 
 
 https://github.com/Avanish474/mlops.git
 
 
 
 4) Now to use jenkins you have to download a software called ngroks for linux os.
 After downloading this software ,paste the software file in your Desktop and open its terminal or type cd /root/Desktop
 Now you just have to type :
 
 
 ./ngrok http 8080
 
 
 Next think to do is to type your IP:8080 (ex. 192.168.53.205:8080) in your browser .This will navigate your to Jenkins.
 
 5) Create new jobs in Jenkins like said in the above topics regarding the task desciption
 
 
  # JOB1 : called the Githubjob
  #Note : Give root privileges to the jenkins user, if you have not done it already by doing the following
   
   
   echo "jenkins        ALL=(ALL)       NOPASSWD: ALL" >> etc/sudoers
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/1%5B1%5D.jpg)
 
 
  ![Image description](https://github.com/Avanish474/mlops/blob/master/2%5B1%5D.jpg)
 
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/3%5B1%5D.jpg)
 
 
  # JOB2: called start
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0025%5B1%5D.jpg)
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0027%5B1%5D.jpg)
 
 
  # JOB3: called trainandpredict
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0031%5B1%5D.jpg)
  
 
  
  
  # JOB4: called accuracy
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/WhatsApp%20Image%202020-05-26%20at%206.12.48%20PM.jpeg)

  
  # JOB5: called notification
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0034%5B1%5D.jpg)
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0038%5B1%5D.jpg)
 
 
 
  # JOB6: called job6
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0040%5B1%5D.jpg)
  
  
  ![Image description](https://github.com/Avanish474/mlops/blob/master/IMG-20200526-WA0042%5B1%5D.jpg)
  

  
# Well ,you have achieved what you wanted and now you can write your own python scripts or work with some jenkins plugins to make your project more effective.
   
 
