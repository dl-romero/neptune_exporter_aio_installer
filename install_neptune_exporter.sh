#!/bin/bash
read -p "What is your current linux username? " current_linux_user
yes | pip3 install -r apps/neptune_exporter/requirements.txt
sudo mkdir /etc/neptune_exporter
sudo cp -R apps/neptune_exporter/* /etc/neptune_exporter
sudo cp apps/neptune_exporter/neptune_exporter.service /etc/systemd/system
sudo chown $current_linux_user:$current_linux_user -R /etc/neptune_exporter
sudo sed -i -e "s/<USERNAME>/$(current_linux_user)/g" /etc/systemd/system/neptune_exporter.service
sudo systemctl daemon-reload
sudo systemctl start neptune_exporter
sudo systemctl enable neptune_exporter
sudo systemctl status neptune_exporter
