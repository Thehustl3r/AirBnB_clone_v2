#!/usr/bin/env bash
# the script that will configure the web server

# install nginx if doesn't exit
if ! command -v nginx &> /dev/null; then
	sudo apt-get update && sudo apt-get install nginx -y
fi

# create necessary directory if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# create a fake HTML file for testing
echo "
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create or recreate a symblolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data folder to the ubuntu user
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration to serve rhe content
echo "
server {
	listen 80;
	server_name _;

	location /hbnb_static {
		alias /data/web_static/current;
	}

	location / {
		index index.html
	}
}" | sudo tee /etc/nginx/sites-available/default

# test configuration
nginx -t > /dev/null

# Restart Nginx to apply the changes
sudo service nginx restart
