import math
n=int(input('enternumber'))
if(n%2==1):
    a=1
    r=2
    series=(n+1)/2
    result=2**(series-1)
    print(result)
else:
    a=1
    r=3
    series=n/2
    result=3**(series-1)
    print(result)
