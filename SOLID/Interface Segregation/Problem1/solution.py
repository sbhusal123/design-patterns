from abc import ABC, abstractmethod


class MobileDevice(ABC):
    """
    Interface:
    --------------------------------------------------------
    Signature for creating normal mobile device object
    Doesnt enforces the client/class to implement GPS func.
    --------------------------------------------------------
    """
    @abstractmethod
    def call(self, number):
        raise NotImplementedError
    
    @abstractmethod
    def send_sms(self, number, message):
        raise NotImplementedError


class WithGPS(MobileDevice):
    """
    This interface is to be only used by the mobile device 
    that supports GPS.
    """
    @abstractmethod
    def activate_gps(self):
        raise NotImplementedError


class DeviceWithGPS(WithGPS):

    def call(self, number):
        print(f"Calling {number}")
    
    def activate_gps(self):
        print("Activated gps.")

    def send_sms(self, number, message):
        print(f"Sent {message} to {number}")


class DeviceWithoutGPS(MobileDevice):

    def call(self, number):
        print(f"Calling {number}")

    def send_sms(self, number, message):
        print(f"Sent {message} to {number}")


if __name__ == "__main__":
    d1 = DeviceWithGPS()
    d1.activate_gps()
    d1.call("4567")

    d2 = DeviceWithoutGPS()
    d2.call("12345")
