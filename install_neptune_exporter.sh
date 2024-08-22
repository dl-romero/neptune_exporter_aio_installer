#!/bin/bash
$user_running_script = whoami
sudo mkdir /etc/neptune_exporter
sudo cp -R apps/neptune_exporter/* /etc/neptune_exporter
sudo cp apps/neptune_exporter/neptune_exporter.service /etc/systemd/system
sudo sed -i -e "s/<USERNAME>/$(whoami)/g" /etc/systemd/system/neptune_exporter.service
sudo systemctl daemon-reload
sudo systemctl start neptune_exporter
sudo systemctl enable neptune_exporter
sudo systemctl status neptune_exporter



