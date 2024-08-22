# Neptune Exporter
### Export Apex / Fusion monitoring metrics for Prometheus.

This has been exporter has been tested on CentOS 7 and Rocky 9.<br>

Python Versions Verified: Python 3.9.18

Before getting started you should collect some information and have it ready. You'll be asked for it later.

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
wget http://github.com/rest_of_url_to_file_.linux-amd64.tar.gz
tar -xvzf file_name_.linux-amd64.tar.gz
```

Neptune Exporter Installation Instructions:
```
cd /tmp/neptune_exporter_vX
./install_neptune_exporter.sh
```

Manage Configurations:

    _Fusion_:
        Configuration File: /etc/neptune_exporter/configuration/fusion.yml

        ```
        sudo vi /etc/neptune_exporter/configuration/fusion.yml
        ```
 
    _Apex_:
        Configuration File: /etc/neptune_exporter/configuration/apex.yml

        ```
        sudo vi /etc/neptune_exporter/configuration/apex.yml
        ```

        The default file looks like this. You can add, remove, modify the apex_auths as long as its in Yaml format.

        ```
        apex_auths:
          default:
            username: admin
            password: 1234
            # Add as many authentication modules as you would like below these lines. 
            # Helpful if you have multiple Apex with differrent login credentials.
          custom:
            username: ""
            password: ""
        ```

        If you add, remove, modify any of the apex_auths (outside of the username/password), you most likely need to update the prometheus.yml file as well.

### _Other App Install Scripts_
Prometheus
This installer script should only be used for fresh installations of Prometheus.
It will generate a custom prometheus.yml file that Prometheus needs to collect data from Fusion and your Apex.

Warning: Continue at your own risk. Especially if you have Prometheus installed already.
Installation Instructions:
```
cd /tmp/neptune_exporter_vX
sudo ./install_prometheus.sh
```

Grafana Installation Instructions:
This installer script should only be used for fresh installations of Grafana.
Warning: Continue at your own risk. Especially if you have Grafana installed already.
```
cd /tmp/neptune_exporter_vX
sudo ./install_grafana.sh
```
