from oop.inheritance import Developer

class Employee:
    hike = 1.04

    def __init__(self, first_name:str, last_name:str, pay:int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def revised_pay(self):
        return self.hike * self.pay

    # def __repr__(self) -> str:
    #     return (f"Employee({self.first_name}, {self.last_name}, {self.pay})")

    # def __str__(self) -> str:
    #     return (f"name : {self.first_name} {self.last_name}, pay : {self.pay}")

    def __add__(self, other):
        if(isinstance(other, Employee)):
            return self.pay + other.pay
        return NotImplemented



emp = Employee("raj", "kumar", 10000)

#print(emp)

#repr(emp)
#str(emp)

# print(1+2)
# print(int.__add__(1,2))

# print('a'+'b')
# print(str.__add__('a', 'b'))

emp2 = Developer("saurabh", "sastri", 20000, "java")

print(emp+emp2)

