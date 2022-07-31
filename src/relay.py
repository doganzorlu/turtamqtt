from turta_iothat import Turta_RelayController

class RelayController:
    def __init__(self):
        self.controller = Turta_RelayController.RelayController()

    def status(self, channel):
        return 'ON' if rc.read_relay_state(channel) else 'OFF'

    def open(self, channel):
        rc.set_relay(channel, True)
        return rc.read_relay_state(channel) == True
    
    def close(self, channel):
        rc.set_relay(channel, False)
        return rc.read_relay_state(channel) == False
