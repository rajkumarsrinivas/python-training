# class Employee:
#     no_of_emps = 0
#     hike = 1.04

#     def __init__(self, first_name:str, last_name:str, pay:int) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         first = first_name
#         Employee.no_of_emps += 1

#     def fullname(self) -> str:
#         return f"{self.first_name} {self.last_name}"

#     def revised_pay(self):
#         return Employee.hike * self.pay

#     @classmethod
#     def set_hike_amt(cls, amount):
#         cls.hike = 1.1

# emp1 = Employee("rajkumar", "s", 10000)

# print(f"emp1.revised_pay() ==> {emp1.revised_pay()}")
# emp1.set_hike_amt(1.10)
# print(f"emp1.revised_pay() ==> {emp1.revised_pay()}")

class Employee:
    no_of_emps = 0
    hike = 1.04

    def __init__(self, first_name:str, last_name:str, pay:int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        first = first_name
        Employee.no_of_emps += 1

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def revised_pay(self):
        return Employee.hike * self.pay

    @classmethod
    def set_hike_amt(cls, amount):
        cls.hike = 1.1

    @staticmethod
    def multiply(val1, val2):
        return val1*val2
    
emp1 = Employee("rajkumar", "s", 10000)

print(f"emp1.revised_pay() ==> {emp1.revised_pay()}")
emp1.set_hike_amt(1.10)
print(f"emp1.revised_pay() ==> {emp1.revised_pay()}")

print(emp1.multiply(2, 3))

#diff between static and class method.
"""
Static methods, much like class methods, are methods that are bound to a class rather than its object.

They do not require a class instance creation. So, they are not dependent on the state of the object.

The difference between a static method and a class method is:

    1. Static method knows nothing about the class and just deals with the parameters.
    2. Class method works with the class since its parameter is always the class itself.
"""
