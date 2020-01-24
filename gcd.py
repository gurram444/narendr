import math
def gcd(a,b):
    if b==0:
        return a
    else:
        gcd(b,a%b)
a=int(input('enter first number:'))
b=int(input('enter second number'))
GCD=math.gcd(a,b)
print('gcd is:',GCD, end='')


