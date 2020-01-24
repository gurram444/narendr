class x:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a//self.b
a=x(6,3)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

def f(a,b):
    return a+b
c=f(2,3)
print(c)


m=[78,76,89,9,10]     #2nd max element
first=-1
second=-1
for num in m:
    if num>first:
        second=first
        first=num
    elif num<first and num>second:
        second=num
print(second)
print(first)