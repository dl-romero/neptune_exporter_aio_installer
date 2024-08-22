# Neptune Exporter
### Export Apex / Fusion monitoring metrics for Prometheus.

This exporter has been tested on CentOS 7 and Rocky 9.<br>

Python Versions Verified: Python 3.9.18

Before getting started you should collect some information and have it ready. You'll be asked for it later if using the installer scripts.

#### _Neptune Fusion_
 - Your username & password for Fusion. Verify your credentials work by logging into https://apexfusion.com/login
 - All Apex IDs of your Apex devices.
    - Once logged into Fusion. Go to https://apexfusion.com/apex to show all your Apex devices.
    - Click on the first Apex device. You will notice the URL will change. Copy everything after the last slash. This is the Apex ID. Repeat this process if you have multiple Apex devices. Example if the url becomes https://apexfusion.com/apex/etn990l983hcigb9j39sfjtjyhvf9efc then your Apex ID of that device is "etn990l983hcigb9j39sfjtjyhvf9efc"

#### _Neptune Apex_
 - Your Apex IP Adress. Easiest way of getting this is to use the Fusion App.
    - In the App. Click on the 3 gears icon.
    - Click the WiFi icon.
    - Scroll down if needed, but look for the IP Address. Note this down.
 - Your Neptune Apex username & password. This may be the default, or you could have changed it.
    - If its default. The login will be username: admin, password: 1234.
    - Verify this works by going to http://your_ip_address_here in your web browser and testing the login.

#### Download & Unpack Instructions:
```
cd /tmp
wget http://github.com/rest_of_url_to_file_.linux-amd64.tar.gz
tar -xvzf file_name_.linux-amd64.tar.gz
```

#### Neptune Exporter Installation Instructions:
```
cd /tmp/neptune_exporter_vX
./install_neptune_exporter.sh
```

### Manage Configurations:
#### Fusion:
Configuration File: /etc/neptune_exporter/configuration/fusion.yml<BR>
You can add, remove, modify the apex_systems as long as its in Yaml format.<BR>
If you add, remove, modify any of the apex_systems (outside of the username/password), you most likely need to update the prometheus.yml file as well.<BR>
<BR>
Sample: [fusion.yml](https://github.com/dl-romero/neptune_exporter/blob/main/apps/neptune_exporter/configuration/fusion.yml) 
 
#### Apex:
Configuration File: /etc/neptune_exporter/configuration/apex.yml<BR>
You can add, remove, modify the apex_auths as long as its in Yaml format.<BR>
If you add, remove, modify any of the apex_auths (outside of the username/password), you most likely need to update the prometheus.yml file as well.<BR>
<BR>
Sample: [apex.yml](https://github.com/dl-romero/neptune_exporter/blob/main/apps/neptune_exporter/configuration/apex.yml) 

#### Prometheus:
Configuration File: /etc/prometheus/prometheus.yml<BR>
To scrape metrics from your Apex(s) directly and or for from Fusion you will need to add the job into your Prometheus Scrape Configs in the prometheus.yml.<BR>
<BR>
Sample: [prometheus.yml](https://github.com/dl-romero/neptune_exporter/blob/main/apps/prometheus/prometheus.yml) 

### _Other App Install Scripts_
NOTE: These scripts were written for those who - 1. Do not have the app installed, 2. Have no familiarity installing and configuring these Apps and just want to get things up and running.<BR>
#### Prometheus
This installer script should only be used for fresh installations of Prometheus.
It will generate a custom prometheus.yml file that Prometheus needs to collect data from Fusion and your Apex.<BR>
<BR>
Warning: Continue at your own risk. Especially if you have Prometheus installed already.
Installation Instructions:
```
cd /tmp/neptune_exporter_vX
sudo ./install_prometheus.sh
```

#### Grafana Installation Instructions:
This installer script should only be used for fresh installations of Grafana.<BR>
<BR>
Warning: Continue at your own risk. Especially if you have Grafana installed already.
```
cd /tmp/neptune_exporter_vX
sudo ./install_grafana.sh
```
