#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static.

# Check if nginx already exists before trying to install afresh
if [[ ! -x /usr/sbin/nginx ]];
then
    sudo apt-get -y update
    sudo apt-get install -y nginx
fi

# Make the necessary directories if they don't already exist
if [[ ! -d "/data/web_static/releases/test/" ]];
then
    mkdir -p /data/web_static/releases/test/
fi

if [[ ! -d "/data/web_static/shared/" ]];
then
    mkdir -p /data/web_static/shared/
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
sudo chown -R ubuntu:ubuntu /data/

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
