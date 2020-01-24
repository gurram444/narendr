a=['hey','bro!','how','are','you']
itr=iter(a)
print(next(itr))
print(next(itr))


class test:
    def __init__(self,limit):
        self.limit=limit

    def __iter__(self):
        self.x=10
        return self

    def __next__(self):
        x=self.x
        if x>self.limit:
            raise StopIteration
        self.x=x+1
        return x
t=test(15)
it=iter(t)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except(StopIteration):
    pass


