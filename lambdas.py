nums=[2,4,3,5,6,7,86,4,51,32,66,77]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
odds=list(filter(lambda a:a%2!=0,nums))
print(odds)
print(evens+odds)
n=[2,4,6,8]
doubles=list(map(lambda n:n*2,n))
print(doubles)

from functools import reduce
sum=reduce(lambda a,b:a+b,odds)
print(sum)

l=['2','3','5','7','9']
ls=list(map(int,l))
print(ls)