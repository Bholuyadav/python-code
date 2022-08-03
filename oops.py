class Employee:
   def __init__ (self,first,last,income):           
    self.first= first            
    self.last= last           
    self.income= income  

   def printdetails(self):
       print(f"the name is {self.first}.the last name is {self.last} and income is {self.income}")       

emp_1=Employee('Dheeraj', 'yadav', '5000')

emp_2=Employee('suraj','ahir',1000)

print(emp_1.first)