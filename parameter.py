def add(a,*b):
    c=a
    for i in b:
        c=c+i
    print(c)
add(1,2,3,4,5)


def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('nari',age=23,mob=8374411075,city='mumbai')


def count(lst):    #count number of evens and odds in list
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[23,24,25,26,27,28,29]
even,odd=count(lst)
print('even:{} and odd:{}'.format(even,odd))