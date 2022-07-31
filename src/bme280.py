from turta_iothat import Turta_BME280
slp = 760 #Update this from weather forecast to get precise altitude
p_diff = 280

class BME280:
    def __init__(self):
        self.bme280 = Turta_BME280.BME280Sensor()

    def temperature(self):
        return round(self.bme280.read_temperature(), 1)
    
    def humidity(self):
        return round(self.bme280.read_humidity(), 1)

    def rawpressure(self):
        return self.bme280.read_pressure() / 100

    def pressure(self):
        return round(self.rawpressure + p_diff, 1)

    def altitute(self):
        return round(self.bme280.read_altitude(round(rawpressure,1)), 1)