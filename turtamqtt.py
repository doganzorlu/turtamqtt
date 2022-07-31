from src.mqtt import MQTT
from src.bme280 import BME280

import time
import confuse

class HatService:
    def __init__(self):
        print('Service is initializing..')
        self.config = confuse.Configuration('turtamqtt', __name__)

    def start(self):
        print('Service is starting...')
        self.MQTT = MQTT(
            broker=self.config['service']['broker'].get(),
            prefix=self.config['service']['prefix'].get(),
            location=self.config['service']['location'].get(),
            username=self.config['service']['username'].get(),
            password=self.config['service']['password'].get())

        Temperature = self.MQTT.add_topic(
                component='sensor',
                name='temperature',
                device_class='temperature',
                unit_of_measurements='°C')
        
        Humidity = self.MQTT.add_topic(
                component='sensor',
                name='humidity',
                device_class='humidity',
                unit_of_measurements='RH')

        self.bme = BME280()

        while True:
            Temperature.publish(self.bme.temperature())
            Humidity.publish(self.bme.humidity())
            time.sleep(20)

if __name__ == '__main__':
    hatservice = HatService()
    hatservice.start()