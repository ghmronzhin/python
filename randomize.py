import copy
from random import shuffle
import collections

neqFlag = True 
d1 = [1, 2, 3, 4, 5, 6]
d2 = copy.copy(d1)
shuffle(d2)
shflN = 0
while(neqFlag):
    print(d1)
    print(d2)
    if str(d1) != str(d2):
        print(d1)
        print(d2)
        shuffle(d2)
        shflN+=1
    else:
        neqFlag = False
print(shflN)
    
