class Flat:
    makanmalik ="soumya"
    def __init__(self,name,occupation,income):
        self.name = name
        self.occupation = occupation
        self.income = income

    def info(self):
        print(f"name is {self.name}.the occupation is {self.occupation}\
            and the income is {self.income}")
    
Dheeraj=Flat('dheeraj', 'student' , '0')
Gautam= Flat('gautam', 'software engineer', '6000')
Chandan= Flat('chandan', 'flipkart', '21000')

# print(Dheeraj.makanmalik
# )
print(Dheeraj.info())