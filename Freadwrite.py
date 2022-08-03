actress_file=open('pornactress.txt','r')
# print(actress_file.readable())
# This line will print true to make sure that file is readable


# print(actress_file.readlines())
# this upper line will print every thing in your files whatever you have


for lines in actress_file:
    print(lines)
    # this upper line of for loop is amazing print line in amazing way

actress_file.close()