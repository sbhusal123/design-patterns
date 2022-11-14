"""
Reference Taken From: 
https://medium.com/@zackbunch/python-dependency-inversion-8096c2d5e46c
"""

class LightBulb:
    
    def turn_on(self):
        print("Ligh bulb turned on")
    
    def turn_off(self):
        print("Ligh bulb turned off")


class PowerSwitch:
    def __init__(self, bulb: LightBulb) -> None:
        self.light_bulb = bulb
        self.on = False

    def press(self):
        if self.on:
            self.on = False
            self.light_bulb.turn_on()
        else:
            self.on = True
            self.light_bulb.turn_off()


hueBulb = LightBulb()
switch = PowerSwitch(hueBulb)
switch.press()
switch.press()


"""
From tha author
----------------------------------------------------------------------------------------------
In the example above, there is a clear dependency between the lightbulb and the power switch
because the power switch object takes in a lightbulb and then directly calls
the turn off and turn on method on that instance. 

While this code may work and get the job done, it does not satisfy SOLID. 
To adhere to the principle of dependency inversion (the D in SOLID), 
we need to ensure that high-level modules do not depend on low level modules, 
but instead depend on abstractions. 

The abstraction should not depend on details, 
instead the details should depend on abstractions. 
 
Solution:
- apply dependency inversion to remove the dependency of a power switch on the lightbulb. 
  going to need an abstract base class. 
- Abstract base classes are not built into Python, but Python does provide a module that supports abstract classes. 
----------------------------------------------------------------------------------------------
"""