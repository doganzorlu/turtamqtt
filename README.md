# turtamqtt
MQTT Service for Turta IoT HAT for Raspberry

This application is developed to provide a background service for Turta hat to use MQTT backend for communication.

If you have any integration system supports MQTT, easly integrate your HAT into that system. Sample topics are created for homeassistant for sample usage.

# Installation

System preperation:

```code
# apt-get install python3-pip
# update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
# update-alternatives 1 python  /usr/bin/python3 /usr/bin/python
# pip install poetry
````

Installion the application into /opt folder:

```code
# cd /opt
# git clone https://github.com/doganzorlu/turtamqtt.git
# cd /etc/systemd/system
# ln -s /opt/turtamqtt/turtamqtt.service .
# systemctl daemon-reload
# systemctl enable turtamqtt
# mkdir /etc/turtamqtt
# cp /opt/turtamqtt/config.yaml.sample /etc/turtamqtt/config.yaml
# cd /opt/turtamqtt
# poetry install
```
You have to edit variables in **/etc/turtamqtt/config.yaml file and start the service:

```code
# systemctl start turtamqtt
````

That's all.

TODO:

* Create logging subsystem
* Create exception handling mechanism
* Create documentation

