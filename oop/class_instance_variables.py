# class Employee:
#     pass

# emp1 = Employee()
# emp1.first_name = "rajkumar"
# emp1.last_name = "s"
# emp1.pay = 10000

# print(f"{emp1.first_name} {emp1.last_name} - {emp1.pay}")

class Employee:

    hike = 1.04

    def __init__(self, first_name:str, last_name:str, pay:int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        first = first_name

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def revised_pay(self):
        return Employee.hike * self.pay


emp1=Employee("rajkumar", "s", 10000)

# print(emp1.fullname())
# print(emp1.revised_pay())
# print(Employee.hike)
# print(emp1.hike)

# Use 2 employee instance and show the diff of class variable and instance variable

emp2=Employee("aiswarya", "v", 10000)
print("emp2.hike ==> "+str(emp2.hike))
print(f"emp2.revised_pay() ==> {emp2.revised_pay()}")
emp2.hike = 1.10
print(f"emp2.revised_pay() ==> {emp2.revised_pay()}")

print(f"emp2.hike ==> {emp2.hike}")
print(f"Employee.hike ==> {Employee.hike}")

Employee.hike = 1.1

emp3=Employee("priyanka", "v", 10000)
print("emp3.hike ==> "+str(emp3.hike))
print(f"Employee.hike ==> {Employee.hike}")
print(f"emp3.revised_pay() ==> {emp3.revised_pay()}")

emp3=Employee("priyanka", "v", 10000)
print("emp3.hike ==> "+str(emp3.hike))
print(f"Employee.hike ==> {Employee.hike}")
print(f"emp3.revised_pay() ==> {Employee.revised_pay(emp2)}")


# introduce no_of_emps class variable and help them understand it better. 