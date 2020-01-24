def simple():
    yield 1
    yield 2
    yield 3
for i in simple():
    print(i)
x=simple()
print(x.__next__())
print(x.__next__())


def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b

f=fib(5)
try:
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
except(StopIteration):
    pass