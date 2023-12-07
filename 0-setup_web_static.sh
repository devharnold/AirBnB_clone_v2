#!/usr/bin/env bash
#Install Nginx if not currently installed
#And sets up a web server for deployment of web_static


sudo apt-get update
sudo apt-get install -y nginx


sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
echo "Holberton School" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu:ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;


    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    }
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default
service nginx restart