"""
|------------|        |---------------|
|  Employee  |        |   Manager     |
|------------|<|------|---------------|
| name       |        |   department  |
|------------|        |---------------|
|print_emp() |        |   print_emp() |
|save_emp()  |        |   save_emp()  |
|------------|        |---------------|
"""

class Employee:

    def __init__(self, name):
        self.name = name

    def print_emp(self):
        # Implementation here
        pass

    def save_emp(self):
        # implementation here
        pass

class Manager(Employee):

    def __init__(self, name, dep):
        super().__init__(name)
        self.department = dep

    def print_employee(self):
        # Implementation here
        pass
    

def print_employee(e: Employee | Manager):
    e.print_emp()
