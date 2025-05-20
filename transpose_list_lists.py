

import random

n_row = 3
n_col = 3
l = [[int(random.random()*10) for i in range(n_col)]for j in range(n_row)]
for row in l:
    print(*row)

# print (list(zip(l,*l)))
res= list(zip(l))
print(res)
# print(a,b,c)

# * unpacks the list of lists in n lists
# zip joins each value to their corresponding regarding index position: 0 paired with each 0s, 1 with 1s... so we pair the values on the columns
# list(zip) is because zip -> <zip object at memory address>
# map(list, ... ) becausewe want each tuple to be a list
# finally list(everything) because we want to end up again with a list of lists
trans = list(map(list,list(zip(*l))))
print(zip(*l))

print("\n")
for row in trans:
    print(*row)