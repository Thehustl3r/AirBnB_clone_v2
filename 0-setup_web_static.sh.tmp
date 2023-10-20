#!/usr/bin/env bash
# updating the system and installing Nginx

sudo apt-get update
sudo apt-get -y install nginx

# creating the forders mentioned
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# creating the fake Html file
echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' >> /data/web_static/releases/test/index.html

# creating the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changing the ownership of the data forder
sudo chown -R ubuntu:ubuntu /data/

# updating Nginx configuration file
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
#restarting the Nginx
sudo service nginx start
