#!/bin/bash
cd apps/prometheus
sudo yum update -y
sudo yum install wget -y
wget https://github.com/prometheus/prometheus/releases/download/v2.54.0/prometheus-2.54.0.linux-amd64.tar.gz
sudo useradd --no-create-home --shell /bin/false prometheus
sudo mkdir /etc/prometheus /var/lib/prometheus
sudo chown prometheus:prometheus /etc/prometheus
sudo chown prometheus:prometheus /var/lib/prometheus
tar -xvzf prometheus-2.54.0.linux-amd64.tar.gz
sudo mv prometheus-2.54.0.linux-amd64 prometheus
sudo cp prometheus/prometheus /usr/local/bin/
sudo cp prometheus/promtool /usr/local/bin/
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool
sudo cp -r prometheus/consoles /etc/prometheus
sudo cp -r prometheus/console_libraries /etc/prometheus
sudo chown -R prometheus:prometheus /etc/prometheus/consoles
sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries
sudo sed -i -e "s/<YOUR LINUX HOSTNAME HERE>/$(hostname)/g" prometheus.yml
read -p "Enter the IP Address of your APEX device (You can add more manually later.): " apex_ip
sudo sed -i -e "s/<APEX IP ADDRESS GOES HERE>/$(apex_ip)/g" prometheus.yml
read -p "Enter the ID of your APEX device in FUSION (You can add more manually later.): " fusion_id
sudo sed -i -e "s/<APEX IP ADDRESS GOES HERE>/$(fusion_id)/g" prometheus.yml
sudo cp -rf prometheus.yml /etc/prometheus/prometheus.yml
sudo chown prometheus:prometheus /etc/prometheus/prometheus.yml
sudo cp prometheus.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now prometheus
sudo systemctl status prometheus
