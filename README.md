
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
* [Prerequisites](#prerequisites)
* [Usage and Troubleshooting](#usage)




<!-- GETTING STARTED -->
## Getting Started

Build the Image:
=============================

docker build -t igalcohen/myskagam -t igalcohen/myskagam:latest .

Push the image into Docker Hub Repo:
=======================================

you must first have a docker hub account on https://hub.docker.com/ and local repo that is public and not private.

first you must create a public repository 
 
i've named my repository by name of: myskagam
and myusername is igalcohen . so my repository name is : 

igalcohen/myskagam

afterwards we need to tag our image:
 
imagename = our full image name
tagname = is combined from two values our full image name [igalcohen/myskagam] and our custom tag [latest]



below is the full synthax:

sh'''
docker tag [imagename] [tagname]
docker tag igalcohen/myskagam igalcohen/myskagam:latest
'''

finally we push the image to our repo

sh'''
docker push igalcohen/myskagam
'''



### Prerequisites




* Minimum Requirments for running this program
* i5 with 4 cores
* 8GB Ram
* SSD Storage For Faster Deployment
* Vagrant Application Installed  - you can download at : https://www.vagrantup.com/downloads
* OS:Windows 10 , With HyperV Feature Installed



<!-- USAGE EXAMPLES -->
## Usage and Troubleshooting

first look at the vagrantfile and see if it's meets your needs. (make neccsery changes) .


** THIS SCRIPT WON'T PROMPT FOR USERNAME AND PASSWORD FOR THE SMB SHARE **

(HOST Username and Password must be mentioned in order for that to happen.)
see line: 11 - 13

```sh

config.vm.synced_folder ".", "/vagrant", type: "smb",
smb_username: '#########',
smb_password: '#########'
```

```sh

this is a must if we want to export the join command creating the token (see line 69 on master.sh script)
to the localhost and then copy it the slave node( and i know for security reasons this is not idle 
, but you can use environment variables as i mentioned above , see below link ):


you can use Vagrant ENV Plugin For environment variables
can be found on https://github.com/gosuri/vagrant-env
```


and  without pressing any more commands besides the first and only command to run this program : 
just write: 
```sh

vagrant up 
```

and u're on the way.

* Troubleshooting Advices:

   if some reason vagrant won't use the hyperv as provider run this command instead of vagrant up:
```sh

vagrant up --provider=hyperv
```

1. vagrant is stuck while initializing the k8s master node 

   in some cases k8s master won't start normally , the solution is very simple
   just do a reset , after both of the vm's are up

   below are the commands to do so :
```sh
reset K8S with kubeadm
sudo kubeadm reset -f
sudo rm -r /etc/cni/net.d

reset ip tables
sudo iptables -F && sudo iptables -t nat -F && sudo iptables -t mangle -F && sudo iptables -X
sudo systemctl restart kubelet
sudo systemctl restart containerd
rm /home/vagrant/.kube/config

```

   and afterwards you can kube init the cluster normally with commands mentioned on the first script master.sh . (See line 89) 

2. the vagrant will deploy sucessfully but the k8s master node status is not ready.

   sometimes the script won't create the .kube directory on the user home folder .
   so what u need to do is just :

```sh 
vagrant ssh master
mkdir -p /home/vagrant/.kube
sudo cp -i /etc/kubernetes/admin.conf /home/vagrant/.kube/config
sudo chown $(id -u):$(id -g) /home/vagrant/.kube/config

and then check the k8s-cluster status
with the command 

kubectl get cluster-info
```






