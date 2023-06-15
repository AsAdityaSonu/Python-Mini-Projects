#Find all the subset from a set of numbers whose sum is zero
#constraint: Subset size musts be 3 to 6 only
#set={-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4}

import random as r

Set = set([-12, -3, -6, 7, 2, -2, 6, 3, 9, -7, -5, -8, 1, 11, -9, -4])
SetSize = 5
ResultList = set()  

for i in range(1000):
    num = r.sample(Set,SetSize)

    if sum(num) == 0:
        ResultList.add(tuple(num))

for r in ResultList:
	print (r)

print ("\nTotal Sets: ", len(ResultList))
