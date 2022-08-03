class Students:
    no_of_holidays=10

    def __init__(self ,name , last):
        self.name = name
        self.last = last

    def printdetails(self):
        print( f"the name is {self.name} and last name is {self.last}")
    
std_1=Students('Dheeraj', 'Yadav')
std_2=Students('suraj','Ahir')

# std_2.printdetails()
# print(std_1.no_of_holidays)
print(std_2.last)
