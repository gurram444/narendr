li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = list( filter(lambda x: x%2==0, li))
sqare=list(map(lambda x:x**2,evenNumbers))
print(sqare)

l=[76,5,8,9,3,6]                      #sorting list
print(sorted(l,reverse=False))

ld={'id':'narendra','address':'rajesh','name':'naresh','mobile':'lenovo'}    # sorting dict by using values
print(sorted(ld.items(),key=lambda kv:(kv[1] ,kv[0])))

import collections                     # counting elements
cnt=collections.Counter()
ls=['red', 'blue', 'red', 'green', 'blue', 'blue']
for i in ls:
    cnt[i]+=1
print(cnt)
for k,v in cnt.items():
    if v>1:
        print(k,v)

from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20},{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
print(sorted(lis,key=itemgetter('age')))
print(sorted(lis,key=itemgetter('age','name')))