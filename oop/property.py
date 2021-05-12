class Employee:

    def __init__(self, first_name:str, last_name:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        #self.email=first_name+"."+last_name+"@abc.com"

    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # @property
    # def email(self) -> str:
    #     return f"{self.first_name}.{self.last_name}@abc.com"

    # @fullname.setter
    # def fullname(self, name):
    #     self.first_name, self.last_name = name.split(' ')
    
    # @fullname.deleter
    # def fullname(self):
    #     self.first_name =  None
    #     self.last_name = None


emp = Employee("raj", "kumar")

print(emp.first_name)
print(emp.email)
print(emp.fullname)

# emp.fullname = "rajkumar srinivasan"

# print(emp.fullname)
# print(emp.email)

# del emp.fullname
# print(emp.fullname)
# print(emp.email)