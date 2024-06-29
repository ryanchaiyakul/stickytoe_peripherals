import dht
import json


class DHT:

    def __init__(self, model: str, pin: int):
        if model == "dht22":
            self.__sensor = dht.DHT22(pin)
        elif model == "dht11":
            self.__sensor = dht.DHT11(pin)
        else:
            raise ValueError

    def callback(self, msg: str):
        self.__sensor.measure()
        data = {'temperature': self.c_to_f(self.__sensor.temperature()), 'humidity': self.__sensor.humidity()}
        return json.dumps(data)

    @staticmethod
    def c_to_f(c):
        return c * 1.8 + 32

def get_instance(config: dict):
    return DHT(**config)