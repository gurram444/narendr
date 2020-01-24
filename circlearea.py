pi=3.14
r=float(input('enter radius of circle'))
area=pi*r*r
print('area of circle is:', area)



n=int(input('enter year'))
if (n%400==0) or ((n%4==0) and (n%100!=0)):
    print('year is leap year:', n)
else:
    print('this is not leap year')

l=[4,5,2,6,7]
l.insert(2,9)
print(l)