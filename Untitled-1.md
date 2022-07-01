 
task 1
Create a Dockerfile that packages:
An index.html file that outputs current date and time using JavaScript
Nginx web server that serves that file so that:
Nginx execution is the default process for the resulting Docker image
The init process of the resulting container has to run as non-root user
(Bonus level) Use vanilla alpine as your base image

task 2 
Build the image and push it to Docker Hub

task 3 
Prepare deployment code (Helm, Kustomize, plain YAML, Terraform or Ansible ) to deploy your image to K8s.
Expose the process as a Kubernetes Service
In K8s network the service should listen on port 80
You can use https://labs.play-with-k8s.com/ for testing


task 4
Write a test script (in bash or in Python) to check that our container works as expected:
that the web page is served correctly
what is getting returned is a date
(Bonus) - check that the date is correct

task 5 
Create a github repository that holds:
The index.html file
The Dockerfile
K8s deployment in whatever format you chose
The test script
a README.md that explains how to build, push, deploy and test the resulting application

