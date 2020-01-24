import itertools
list=itertools.product('abcd',repeat=2)
list=[i for i in list]
print(list)
l=itertools.repeat(10,3)
l=[i for i in l]
print(l)
l1=itertools.chain('abcd','efgh')
l1=[i for i in l1]
print(l1)
