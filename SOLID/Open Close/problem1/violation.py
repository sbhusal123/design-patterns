class Employee:

    def __init__(self, name):
        self.name = name
    
"""
def print_employee(e):
    print(f"{e.name} is an employee.")
"""



"""
Now we need to exptend the functionality. 

|------------|        |---------------|
|  Employee  |        |   Manager     |
|------------|<|------|---------------|
| name       |        |   department  |
|------------|        |---------------|

As seen above we've  a manager class that inherit from Employee (as Manager is also an employee)

Let's add a functionality.
"""

class Manager(Employee):

    def __init__(self, name, dep):
        super().__init__(name)
        self.department = dep
    

"""Updated version of print employee"""
def print_employee(e: Employee | Manager):
    """This is where things go bad
        If these checks are in multiple places
        the changes becomes reactive.
    """
    if type(e) is Employee:
        print(f"{e.name} is employee.")
    if type(e) is Manager:
        print(f"{e.name} is employee who manager {e.department}.")


"""Other problem caus of those if else"""
def save_employee(e):
    if type(e) is Employee:
        # save employee
        pass
    if type(e) is Manager:
        # save manager
        pass

