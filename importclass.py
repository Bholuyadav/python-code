from oops import Employee

class Worker(Employee):
    area='gorakhpur'


bhola=Worker('bhola', 'yadav', '200')

# print(bhola.area)
# print(bhola.income)
bhola.printdetails()
print(bhola.area)