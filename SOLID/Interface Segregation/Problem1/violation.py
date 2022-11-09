from abc import ABC, abstractmethod


class MobileDevice(ABC):
    """
    Interface:
    --------------------------------------------
    Signature for creating mobile device object
    --------------------------------------------
    """
    @abstractmethod
    def call(self, number):
        raise NotImplementedError
    
    @abstractmethod
    def activate_gps(self):
        raise NotImplementedError
    
    @abstractmethod
    def send_sms(self, number, message):
        raise NotImplementedError



class DeviceWithGPS(MobileDevice):

    def call(self, number):
        print(f"Calling {number}")
    
    def activate_gps(self):
        print("Activated gps.")

    def send_sms(self, number, message):
        print(f"Sent {message} to {number}")


class DeviceWithoutGPS(MobileDevice):

    def call(self, number):
        print(f"Calling {number}")
    
    def activate_gps(self):
        """
        This is exactly what violates the interface segregation principle
        As for this class we dont need to implement the signature that enforces
        us to implement the unwanted method i.e. activate_gps
        """
        raise Exception("This device doesnt supports gps.")

    def send_sms(self, number, message):
        print(f"Sent {message} to {number}")


if __name__ == "__main__":
    d1 = DeviceWithGPS()
    d1.activate_gps()

    d2 = DeviceWithoutGPS()
    d2.activate_gps()