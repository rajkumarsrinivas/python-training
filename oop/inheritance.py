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

# class Developer(Employee):
#     hike = 1.1

# dev1=Developer("raj","kumar",10000)
# dev2=Developer("saurabh","sastri",20000)

# print(dev1.revised_pay())
# print(dev1.hike)
# print(dev2.revised_pay())

# print(help(Developer))

class Developer(Employee):
    hike = 1.1

    def __init__(self, first_name: str, last_name: str, pay: int, prog_lang: str) -> None:
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang
    
    # def __add__(self, other):
    #     return self.pay + other.pay+9999

class Manager(Employee):
    hike = 1.2

    def __init__(self, first_name: str, last_name: str, pay: int, employees=None) -> None:
        super().__init__(first_name, last_name, pay)
        self.employees = set() if employees is None else employees

    def add_employee(self, emp):
        self.employees.add(emp)
    
    def del_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for e in self.employees:
            print("--> "+e.fullname())
    

dev1=Developer("raj","kumar",10000, "java")
dev2=Developer("saurabh","sastri",20000, "python")

mgr1 = Manager("ramesh", "dandu", 30000) 

print(mgr1.print_employees())
mgr1.add_employee(dev1)
mgr1.add_employee(dev2)
mgr1.print_employees()

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))