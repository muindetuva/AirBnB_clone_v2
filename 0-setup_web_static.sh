#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get instal -y nginx

# Make the necessary directories if they don't already exist
if [ ! -d "/data/webstatic/releases/test/" ];
then
    mkdir -p /data/webstatic/releases/test/
fi

if [ ! -d "/data/webstatic/shared/" ]
then
    mkdir -p /data/webstatic/shared/
fi

# Make fake html file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

# Create a symbolic link each time
ln -nsf /data/web_static/releases/test/ /data/web_static/current 

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        location /hbnb_static {
            alias /data/web_static/current/;
        }

        add_header X-Served-By $HOSTNAME;

}" > /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
