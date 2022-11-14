from abc import ABC, abstractmethod

class Switchable(ABC):
    """
    This acts as a contract stating the methods on this classes (rather interface)
    to be implemented for any classes subclassing this.
    """

    @abstractmethod
    def turn_on(self):
        raise NotImplementedError()

    @abstractmethod
    def turn_off(self):
        raise NotImplementedError()


class LightBulb(Switchable):

    def turn_on(self):
        print("Lightbulb: turned on")

    def turn_off(self):
        print("Lightbulb: turned on")


class PowerSwitch:
    """
    This class sort of behaves as a proxy / middleware 
    for our request of delivering request to higher module.
    """

    """
    Note the typing of dependency c.
    -> It's a type of interface, abstract
    -> Instead of depending on a details,
    -> We depend now on abstraction i.e. interface
    """
    def __init__(self, c: Switchable):
        # Now power switch has a depdnedency of classes that inherits Switchable interface
        # this now depends on interface instead of concrete class
        # exposing all the signatures of switchale interface
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.on = False
            self.client.turn_off()
        else:
            self.on = True
            self.client.turn_on()

  
"""
Now we can extend the functionality from LightBulb switching to 
FanSwitching by implementing the same switchable interface.
"""