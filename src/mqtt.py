from paho.mqtt import client as mqtt_client
from src.topic import Topic
import random

class MQTT:
    is_connected = False
    topics = []
    def __init__(self,prefix, location, username, password,broker, port=1883):
        self.broker = broker
        self.port = port
        self.prefix = prefix
        self.location = location
        self.id = '{}/{}'.format(prefix, location)
        self.client_id = f'hatservice-{random.randint(0, 1000)}'
        self.username = username
        self.password = password
        self.client = mqtt_client.Client(self.client_id)
        self.client.on_message = self.on_message
        self.connect()
        self.client.loop_start()

    def add_topic(self, **kwargs):
        kwargs['prefix'] = self.prefix
        kwargs['location'] = self.location
        kwargs['pub_callback'] = self.publish
        topic = Topic(**kwargs)
        self.topics.append(topic)
        return topic

    def on_connect(self, client, userdata, flags, status):
        print('on_connect callback is called')
        if status == 0:
            print('Connected to {} on port {}'.format(self.broker, self.port))
            is_connected = True
        else:
            print('Connection failed to {} on port {} with status code {}'.format(
                self.broker,
                self.port,
                status
                ))
            is_connected = False

    def connect(self):
        self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker, self.port)

    def publish(self, topic, msg):
        result = self.client.publish(topic, msg)
        status = result[0]
        return status

    def on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

# client.on_publish = on_publish
# client.on_subscribed = on_subscribed
# client.on_log = on_log

    def subscribe(self, topic):
        self.client.subscribe(topic)