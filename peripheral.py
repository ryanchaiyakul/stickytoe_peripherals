import mip
import gc

class Peripheral:
    """
    Wrapper class to install and import a valid peripheral package
    """
    _valid_packages = {
        "st_dht": "github:ryanchaiyakul/stickytoe_peripherals/peripherals/rhth/st_dht.py",
        "st_sht31": "github:ryanchaiyakul/stickytoe_peripherals/peripherals/rhth/st_sht31.py"
    }
    _installed_packages = {}

    def __init__(self, uid: str, package: str, config: dict):
        if package not in self._valid_packages.keys():
            raise ValueError

        self.__uid = uid
        self.__package = package

        if self.__package not in self._installed_packages.keys():
            self.__install(self.__package)
            gc.collect()

        self.__instance = self._installed_packages[self.__package].get_instance(
            config)
        if callable(getattr(self.__instance, 'callback', None)) is None:
            raise ValueError

    def callback(self, msg: str):
        return self.__instance.callback(msg)

    @classmethod
    def __install(cls, package: str):
        try:
            cls._installed_packages[package] = __import__(
                package, globals(), locals(), [], 0)
        except ImportError:
            mip.install(cls._valid_packages[package])
            cls._installed_packages[package] = __import__(
                package, globals(), locals(), [], 0)