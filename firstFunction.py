import math
from math import *

friends = ("Jim", "Karen","Kevin")
def cube(num):
    num = math.sqrt(num)
    return num

fristDictionary = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
}


i = 0
while (i<10):
    print(str(i) + " "+fristDictionary.get(i, "Not Valid"))
    i = i + 1

forLoop = 0
for forLoop in range(10):
    print(str(forLoop)+ "<====this is forLoop")

for friend in friends:
    print(friend)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(10, 1))
number = {
    1: "Dog",
    2: "Cat",
    3: "Tiger"
          }
number_grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,30,40],
]
for row in number_grid:
    for col in row:
        print(col)
