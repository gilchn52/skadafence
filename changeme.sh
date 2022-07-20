#!/bin/bash
mkdir -p /home/nginx
chown nginx:nginx /home/nginx
chmod 777 /home/nginx
sed -i '2s/80/8080/' /etc/nginx/conf.d/default.conf
sed -i '3s/80/8080/' /etc/nginx/conf.d/default.conf


