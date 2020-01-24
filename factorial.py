n=int(input('enter number'))
fact=1
if n<0:
    print('sorry factorial does not exists for negative numbers')
elif n==0:
    print('factorial of 0 is 1')
else:
    for i in range(1,n+1):
     fact=fact*i
    print('factorial of',n ,"is",fact)


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
fact(4)


def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result=fact(4)
print(result)