#!/bin/bash

#update / upgrade
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

echo "INFO: updates complete"

sudo pip3 install Flask
sudo pip3 install flask_ask


#SET UP NGROK
unzip /home/pi/ngrok-stable-linux-arm.zip

#start the ngrok server
sudo ./ngrok http 5000
