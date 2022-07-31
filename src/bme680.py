from turta_iothat import Turta_BME680
slp = 760 #Update this from weather forecast to get precise altitude
p_diff = 280

class BME680:
    def __init__(self):
        self.bme680 = Turta_BME680.BME680Sensor()

    def temperature(self):
        return round(self.bme680.read_temperature(), 1)
    
    def humidity(self):
        return round(self.bme680.read_humidity(), 1)

    def rawpressure(self):
        return self.bme680.read_pressure() / 100

    def pressure(self):
        return round(self.rawpressure + p_diff, 1)

    def altitute(self):
        return round(self.bme680.read_altitude(round(rawpressure,1)), 1)