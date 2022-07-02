
the below program Create on your K8S Cluster an Nginx Unprivileged Container

to build the application you will need a fully functional K8S-Cluster. 

Instructions:


to build the image:
=====================================================================
docker build -t igalcohen/myskagam -t igalcohen/myskagam:latest .


to push the image into docker hub repo:
========================================

you must first have a docker hub account on https://hub.docker.com/ and local repo that is public and not private.


first you must create a public repository 
i've named my repository by name of: 

myskagam

and my username is igalcohen

so my repository name is :

igalcohen/myskagam

afterwards we need to tag our image:

imagename = our full image name
tagname = is combined from two values our full image name [igalcohen/myskagam] and our custom tag [latest]

below is the sythax:

docker tag [imagename] [tagname]
docker tag igalcohen/myskagam igalcohen/myskagam:latest


finally we push the image to our repo
docker push igalcohen/myskagam


to deploy the image:
================================================

login to your K8S-Cluster Machine (on Premiss K8S Cluster / localhost minikube )
run the below command


kubectl apply -f ./deployment.yaml

wait about 60 seconds until the container will be created successfully
2 pods should be running :

one as main container and the other as replica 

you can check and see that our nginx server is operating normally,
by executing the below command:

minikube service nginx-external

your default browser should open and display the current date .


to test that our resulting application:
==================================================
we need python3 in order to use our python script file.
fulltest.py.

to keep our original environment clean let's create a virtual environment on python.

you can achieve that by executing the below command:
python3 -m venv [path_to_you_our_application_directory_[virtual_environment_name]]
for example:

python3 -m venv ~/Projects/myenv

and afterwards install all the needed modules by executing the below command

pip3 install -r req.txt

to test our application:
====================
testing our webpage:
====================
python3 fulltest.py -wp

the browser should open and display the current day 

==========================
testing the date validity:
==========================

python3 fulltest.py -dv test

the program will check and see if the date is valid.

==============================
testing if the date is corret :
==============================

python3 fulltest.py -dc test

the program will check and see if the date is correct

notes:
=============================================
* i've tested the the below on minikube 
* you can name you repo any name you wish , just make sure to apply the changes inside the    
  deployment.yaml file

* i personally recommends using vscode for testing.

* keep you python environment clean and always use a virtual environment .


Best regards
"the treker"
