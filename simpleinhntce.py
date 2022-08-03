class Employee:
    company= "microsoft"
    
    def info(self):
        print("This is an employee")


class Programmer(Employee):
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def infop(self):
        print(f"the name is {self.name} and the surname is {self.surname}")

suraj=Employee()

dheeraj = Programmer('Dheeraj','Yadav')
# print(dheeraj.info())
dheeraj.info()
dheeraj.infop()
suraj.info()
print(suraj.company)
print(dheeraj.company)
# now this is a perfect program you were missing out constructor init when you want to take
# an argument you should use constructor