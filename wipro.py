n = input('enter numbers').split()     # taking numbers from input and remove duplicates from it hddcbcw
print(n)
m = list(map(int, n))
print(m)
output_list = []
for i in m:
    if i not in output_list:
        output_list.append(i)
print(output_list)


def generator(x, y):                  # write function to generate odd number between given range by using generator
    for i in range(x, y):
        if i % 2 != 0:
            yield i
        elif i > y:
            raise StopIteration


x = int(input('enter starting number:'))
y = int(input('enter ending number:'))
obj = generator(x, y)
try:
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())

except(StopIteration):
    print('number exceeded')


l = [10, 15, 20, 25, 30, 35, 45]               # by using filter display elements which are divisible by 15
op = list(filter(lambda x: x % 15 == 0, l))
print(op)


