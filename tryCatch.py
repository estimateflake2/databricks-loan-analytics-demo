from math import *

'''
try :
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("You can't divide by zero: ")
except ValueError as err:
    print("You did not enter a number: ")
    data = [(1,"test",1), (1,"test",1)]
'''
def functionNew (name):
    result =  ("hi: "+ name)
    return result

dict = {1:"Toyota",2:"Honda",3:"BMW"}

for key in dict.keys():
    print(dict[key])

i = 1
while i <= 5:
    print(i)
    i+=1


match functionNew("Joseph"):
    case "hi: Joseph":
        print(functionNew(" your data matched"))
    case "Bankole":
        print(functionNew(" your data did note matched"))
    case _:
        print(functionNew(" problem"))