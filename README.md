

the index.html:

Javascript date object and HTML span element can be used to display the current date and time.
by default Javascript use the browser's timezone to display time and date.

Date object is created with the Date() constructor . Then using innerHTML propety , the content of HTML span element
is set with current date and time.
Unique id of span tag is used by getElementById() method to display the current date and time.

the Nginx Container:
in order to run nginx with non root user we need to change the permission for the below directories&files
/var/cache/nginx
/var/log/nginx
/etc/nginx/nginx.conf

then we create a signal .
nginx can be controlled with signlas.
the process id of the master process for nginx is written to the file /var/run/nginx.pid  by default 
which controls the service.

and take ownership of him as well.

to start the service as nginx user directly. we need to stop it from running as a daemon in the nginx.conf
and we can achieve by the adding the phrase "daemon off" to the nginx.conf file

at the end , we start the process nginx.


task 2 :
Upload my docker image to the my repo
first i create a custom repo on my dockerhub account called
"igalcohen/myskagam"
second:
tag my image:
docker tag myweb:latest igalcohen/myskagam
third:
docker push igalcohen/myskagam
fourth:
u can pull the image with the below command:
docker pull igalcohen/myskagam:latest

task 3:
i used minikube for testing .
i've created three yaml files as configurations (Pod,Deployment and Service)
the POD manifest yaml file , creates a pod and pull the docker image i've uploaded to the the dockerhub repo into the host
afterwards the deployment manifest yaml file , deploys the application on 2 pods , one as main ,and the other as the replica.
the container port set to listen on port 80.
and the final service manifest yaml file , creates a k8s service and expose the container to the Node IP Address
we can check that it works by writeing the below commands:
kubectl get svc
and then copy the service name and paste it on this command
minikube service [servicename] , which will cause the browser to open and display the current date and time.

task 4:










