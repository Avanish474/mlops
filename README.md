# mlops

Have you been thinking to add automation to your machine learning project ? Well here is a way you can make it happen!

#Prerequisites
1) Concepts of redhat operating system commands
2) Basic concepts of Docker 
3) Basics of Git and Github
4) Basics of Jenkins

Note : All above prerequisites should be clear to you if you wanna proceed further .
Setup the softwares listed above in you pc or laptop

![Image description](https://github.com/Avanish474/mlops/blob/93f527b538aea168849ce0dcba94b8509212cb67/mld.jpg


#Task to perform
1. Create container image that has Python3 and Keras or numpy installed using dockerfile

2. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins

3. Job1 : Pull the Github repo automatically when some developers push repo to Github.

4. Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

5. Job3 : Train your model and predict accuracy or metrics.

6. Job4 : if metrics accuracy is less than 80% , then tweak the machine learning model architecture and retrain it.

7. Job5: Notify that the best model is being created

8. Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left


# Solution to above task

1) Create a directory inside your home directory of redhat:
 
   mkdir /project
   
   Go inside this directory:
    
   cd /project
   
   Create an container image having python3 ,keras and numpy previously installed using Dockerfile.Refer to the Dockerfile repository in  
