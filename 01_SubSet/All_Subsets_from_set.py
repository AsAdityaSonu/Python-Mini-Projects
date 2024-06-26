#Find all the subset from a set of numbers whose sum is zero
#constraint: Subset size musts be 5
#set = {-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

import random as r
Set = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
List = set()    

for i in range(10000):
    num = r.sample(Set,5)

    if sum(num) == 0:
        List.add(tuple(num))

for j in List:
	print (j)

print ("\nTotal Sets: ", len(List))