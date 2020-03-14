import requests
import enum
from time import sleep

from traffic_light_simulator import traffic_light_api

class Lights(enum.Enum):
    red = 0
    yellow = 1
    green = 2


class TrafficLight():

    def init_mode(self):
        self.lights = []
        self.on = []
        self.blink = False

    def set_default_mode(self):
        # blink yellow
        self.lights = [1]
        self.on = [500]
        self.blink = 1
        self.activate_mode('2') # blinks minimum twice 

    def set_light(self, light: str, timer: str, blink: bool):
        self.lights.append(Lights[light].value)
        self.on.append(int(timer))
        self.blink = int(blink)

    def activate_mode(self, nbr_of_times='0'):
        ms_delay = 0
        for light_is_on in self.on:
            ms_delay += light_is_on
        minimum_duration_ms = (self.blink + 1) * max(1000, int(ms_delay))
        mode = {'lights': self.lights, 'on': self.on, 'blink': self.blink, 'minimum_duration_ms': minimum_duration_ms}
        requests.post('http://localhost:5000/trafficlight', json=mode)
        sleep((self.blink + 1) * int(nbr_of_times) * minimum_duration_ms/1000) # seconds

if __name__ == '__main__':
    tl = TrafficLight()
    tl.init_mode()
    tl.set_light('yellow', '1000', False)
    tl.set_light('red', '3000', False)
    tl.set_light('yellow', '1000', False)
    tl.set_light('green', '3000', False)
    tl.activate_mode('3')
    tl.set_default_mode()