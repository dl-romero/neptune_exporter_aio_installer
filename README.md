# Neptune Exporter
### Export Apex / Fusion monitoring metrics for Prometheus.

This has been exporter has been tested on CentOS 7 and Rocky 9, but should work on other distros.<br>

Python Versions Verified: Python 3.9.18

Before getting started your going to need collect some information. Youll be asked for it later.

_Neptune Fusion_
 - Your username & password for Fusion. Verify they work by logging into https://apexfusion.com/login
 - All Apex IDs of your Apex devices.
    - Once logged into Fusion. Go to https://apexfusion.com/apex to show all your Apex devices.
    - Click on the first Apex device. You will notice the URL will change. Copy everything after the last slash. This is the Apex ID. Repeat this process if you have multiple Apex devices.

_Neptune Apex_
 - Your Apex IP Adress. Easiest way of getting this is to use the Fusion App.
    - In the App. Click on the 3 gears icon.
    - Click the WiFi icon.
    - Scroll down if needed, but look for the IP Address. Note this down.
 - Your Neptune Apex username & password. This may be the default, or you could have changed it.
    - If its default. The login will be username: admin, password: 1234.
    - Verify this works by going to http://your_ip_address_here in your web browser and testing the login.

Download & Unpack Instructions:
```
cd /tmp
wget http://github.com/rest_of_url_to_file
tar -xvzf file_name.tar.gz
```

Neptune Exporter Installation Instructions:
```
cd /tmp/neptune_exporter_vX
./install_neptune_exporter.sh
```

Prometheus Installation Instructions:
```
cd /tmp/neptune_exporter_vX
sudo ./install_prometheus.sh
```

Grafana Installation Instructions:
```
cd /tmp/neptune_exporter_vX
sudo ./install_grafana.sh
```
