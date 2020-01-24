n=int(input('enter number'))
if n%2==0:
    number=n/2
    series=number-1
    k=3
    print(series)
else:
    number=(n+1)/2
    series=number-1

    x=2*series
    print(x)


import os
p=os.listdir('C:/Users/gurra/PycharmProjects')
print(p)
#help(os)
import random
print(random.seed(3))