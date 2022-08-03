class Programmer:
    company="sprinkler"
    def __init__(self ,name,work):
        self.name = name
        self.work = work
    def printdetails(self):
        print(f"the name is {self.name} and the work is {self.work}")  
       
    
dheeraj = Programmer("dheeraj", "skype")                          
prg_2 = Programmer("suraj", "Ahir")

dheeraj.printdetails()
