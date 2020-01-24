import copy                 #deepcopy
l1=[1,2,[3,5],4]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l2[2][0]=7
print (l2)
print(l1)


l3=[1,2,[3,5],4,6]           #shallow copy
l4=copy.copy(l3)
print(l3)
print(l4)
l3[2][0]=7
print(l3)
print(l4)