# Neptune Exporter
### Export Apex / Fusion monitoring metrics for Prometheus.

This exporter has been tested on fresh install of Rocky 9.<br>
Python Versions Verified: Python 3.9.18

Before getting started you should collect some information and have it ready. You'll be asked for it later if using the installer scripts.

#### _Neptune Fusion_
 - Your username & password for Fusion. Verify that your credentials work by logging into https://apexfusion.com/login
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

#### Getting Started - Neptune Exporter, Prometheus & Grafana Installation Instructions:
```
cd /tmp
wget http://github.com/neptune_exporter.beta.linux-amd64.tar.gz
tar -xvzf neptune_exporter.beta.linux-amd64.tar.gz
mv neptune_exporter.beta.linux-amd64 neptune_exporter
sudo yum install -y python3-pip
cd /tmp/neptune_exporter
pip3 install -r requirements.txt
python3 config_builder.py
chmod 777 *.sh
sudo ./install_grafana.sh
sudo ./install_neptune_exporter.sh
sudo ./instal_prometheus.sh
sudo firewall-cmd --premanent --add-port={9090,3000,5006}/{tcp,udp}
```

#### Check Services
Grafana = http://<hostname/ipaddress>:3000
Prometheus = http://<hostname/ipaddress>:9090 unless you change the port to something else.
Neptune Exporter: http://<hostname/ipaddress>:5006

#### Troubleshooting
If you notice as "server misbehaving" message. 
```
Get "http://pikachu.local:5006/metrics/apex?auth_module=default&target=192.168.1.12": dial tcp: lookup pikachu.local on 192.168.1.1:53: server misbehaving
```
Check your "/etc/hosts file."
```
[me@pikachu ~]$ cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.1.53 pikachu.local
```
You should see 3 lines. If not youll need to add it.
```
sudo vi /etc/hosts
press insert key
got to bottom of the file. Enter the ip address of the server hosting the Neptune Exporter a space and the hostname.
```

### Manage Configurations:
#### Fusion:
Configuration File: /etc/neptune_exporter/configuration/fusion.yml<BR>
You can add, remove, modify the apex_systems as long as its in Yaml format.<BR>
If you add, remove, modify any of the apex_systems (outside of the username/password), you most likely need to update the prometheus.yml file as well.<BR>
<BR>
Sample: [fusion.yml](https://github.com/dl-romero/neptune_exporter/blob/main/documentation/fusion.yml) 
 
#### Apex:
Configuration File: /etc/neptune_exporter/configuration/apex.yml<BR>
You can add, remove, modify the apex_auths as long as its in Yaml format.<BR>
If you add, remove, modify any of the apex_auths (outside of the username/password), you most likely need to update the prometheus.yml file as well.<BR>
<BR>
Sample: [apex.yml](https://github.com/dl-romero/neptune_exporter/blob/main/documentation/apex.yml) 

#### Prometheus:
Configuration File: /etc/prometheus/prometheus.yml<BR>
Sample: [apex.yml](https://github.com/dl-romero/neptune_exporter/blob/main/documentation/prometheus.yml) 
