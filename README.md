
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="git@gitlab.com:gilchn52/k8s-hyperv-deploy.git">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Deploy Nginx Unvprileged Container On K8S Cluster</h3>

  <p align="center">
    the below program Create on your K8S Cluster an Nginx Unprivileged Container

to build the application you will need a fully functional K8S-Cluster. 
i've used minikube  .
    <br />

  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Getting Started](#getting-started)
* [Notes](#Notes)




<!-- GETTING STARTED -->
## Getting Started

Build the Image:
=============================

docker build -t igalcohen/myskagam -t igalcohen/myskagam:latest .

Push the image into Docker Hub Repo:
=======================================

you must first have a docker hub account on https://hub.docker.com/ and local repo that is public and not private.

* first you must create a public repository 
 
  i've named my repository by name of: #myskagam
  and myusername is #igalcohen . so my repository name is : 

  igalcohen/myskagam


* second we need to tag our image:
 
  imagename = our full image name

  tagname = is combined from two values our full image name [igalcohen/myskagam] and our custom tag [latest]

  below is the full synthax:
  
  ```sh
  docker tag [imagename] [tagname]
  ```

  ```sh
  docker tag igalcohen/myskagam igalcohen/myskagam:latest
  ```
  
* third we push the image to our repo

  ```sh
  docker push igalcohen/myskagam
  ```

Deploy the image:
=================

login to your K8S-Cluster Machine (on Premiss K8S Cluster / localhost minikube )
run the below command

```sh
kubectl apply -f ./deployment.yaml
```
wait about 60 seconds until the container will be created successfully
2 pods should be running :

one as main container and the other as replica 
you can check and see that our nginx server is operating normally,by executing the below command:

```sh
minikube service nginx-external
```

your default browser should open and display the current date .

Test our Resulting Application:
===============================
* we need python3 in order to use our python script file.
 fulltest.py.

* to keep our original environment clean let's create a 
  virtual environment on python.

  you can achieve that by executing the below command:

  ```sh
  python3 -m venv [path_to_you_our_application_directory_[virtual_environment_name]]
  ```

  For Example:
  ```sh
  python3 -m venv ~/Projects/myenv
  ```

  and afterwards install all the needed modules by executing the below command

  ```sh
  pip3 install -r req.txt
  ```

 * to test our application with fullacess script:

 1. testing the webpage :
   
   ```sh
   python3 fulltest.py -wp test
   ```

   the browser should open and display the current day 

2. testing the date validity:
   
    ```sh
    python3 fulltest.py -dv test
    ```
    the program will check and see if the date is valid.

3. testing if the date is corret :

   ```sh
   python3 fulltest.py -dc test
   ```
   the program will check and see if the date is correct




<!-- Notes -->
## Notes

* i've tested the the below on minikube 
* you can name your repo any name you wish , just make sure to apply the changes inside the    
  deployment.yaml file

* i personally recommends using vscode for testing.

* keep your python environment clean and always use a 
  virtual environment .

  Best Regards
  "The Treker"







