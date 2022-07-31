import json

class Topic:
    def __init__(self, **kwargs):
        self.prefix = kwargs['prefix']
        self.location = kwargs['location']
        self.name = kwargs['name']
        self.component = kwargs['component']
        self.device_class = kwargs['device_class']
        self.unit_of_measurements = kwargs['unit_of_measurements']
        self.id = '{}/{}/{}/{}'.format(self.prefix, self.component, self.location, self.name)
        self.discovery_topic = '{}/config'.format(self.id)
        self.state_topic = '{}/state'.format(self.id)
        self.cmd_topic = '{}/set'.format(self.id)
        self.pub_callback = kwargs['pub_callback']

        self.discovery()

    def publish(self, value):
        msg = json.dumps(
            {
                self.name: value
            })

        status = self.pub_callback(self.state_topic, msg)
        if status == 0:
            print('Send {} to topic {}'.format(msg, self.state_topic))
        else:
            print('Failed to send message to topic {}'.format(self.state_topic))
    
    def on_message(self, userdata, msg):
        pass
    
    def discovery(self):
        device_config = {
            "~": self.id,
            "name": self.name,
            "unique_id": '{}_{}'.format(self.location, self.name),
            "device_class": self.device_class,
            "unit_of_measurement": self.unit_of_measurements,
            "value_template": '{{ value_json.' + self.name + ' }}',
            "cmd_t": "~/set",
            "stat_t": "~/state",
            "schema": "json",
        }

        status = self.pub_callback(self.discovery_topic, json.dumps(device_config))
        if status == 0:
            print('Send {} to discovery topic {}'.format(json.dumps(device_config), self.discovery_topic))
        else:
            print('Failed to send message to topic {}'.format(self.discovery_topic))

    def set_state(self, value):
        pass
