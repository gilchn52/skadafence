#!/usr/bin/env bash
var1="pid        /var/run/nginx.pid;"
var2="pid        /tmp/nginx.pid;"
sed -i "s|$var1|$var2|g" /etc/nginx/nginx.conf


sed -e '12,30d' /etc/nginx/nginx.conf
cat << EOF >> /etc/nginx/nginx.conf
http {
    client_body_temp_path /tmp/client_temp;
    proxy_temp_path       /tmp/proxy_temp_path;
    fastcgi_temp_path     /tmp/fastcgi_temp;
    uwsgi_temp_path       /tmp/uwsgi_temp;
    scgi_temp_path        /tmp/scgi_temp;
...
}
EOF



