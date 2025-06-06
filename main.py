from math  import *

math = sqrt(3)
subFriends = ["James1","Jordan1","Jacob1"]
friends = ["James","Jordan","Jacob"]
friends1 = friends

data = input("test: ")


if data == "test":
    print(subFriends)
elif data.__contains__("test"):
    print(friends[0])
else:
    print(data)


#for friend in friends: print("my friend's name is: "+friend)