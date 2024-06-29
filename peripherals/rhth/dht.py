import dht

class DHT:

    def __init__(self, model: str, pin: int):
        if model == "dht22":
            self.__sensor = dht.DHT22(pin)
        elif model == "dht11":
            self.__sensor = dht.DHT11(pin)
        else:
            return ValueError

def get_instance(config):
    pass

def hello_world():
    print("hi from dht")