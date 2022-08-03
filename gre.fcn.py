def greatest_numbers(n1,n2,n3):
    if n1>n2:
        return n1
    elif n2>n3:
        return n2
    elif n3>n1:
        return n3
n1=int(input('enter your first num:'))
n2=int(input('enter your second num:'))
n3=int(input('enter your third num:'))
 
print(greatest_numbers(n1,n2,n3))