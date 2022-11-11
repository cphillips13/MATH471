import math

list = [0,1,2,3,4,5,6,7,8,9]
print("Original list {}".format(list))
for j in range(4):
    for i in range(10):
        list[i] = (3*list[i]+7)%10
    print("k = {} and list = {}".format(j, list))

