lists=[3,2,4,13,10,8,9,17]             #print all evens along with odd numbers
a=[]
b=[]
for i in lists:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(sorted(a)+sorted(b))

c=list(filter(lambda n:n%2==0,lists))       #2 solution
d=list(filter(lambda n:n%2!=0,lists))
print(c+d)

list1=[13,2,5,34,52,66,45]           # swap first element with last element viseversa
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)

l=[3,4,6,12,8,9,35]                # sum of list
sum=0
for i in l:
    sum+=i
print(sum)

l1=[4,65,33,63,22,31,6]            # print last n elements from list
l1.reverse()
print(l1)
s=int(input('enter how many numbers u want:'))
c=[]
for i in range(s):
    c.append(l1[i])
print(c)


n=4323                                   #print * based on digits line by line
m = [int(i) for i in str(n)]
for i in m:
    for _ in range(i):
        print("*",end="")
    print()


from collections import defaultdict
string='narendra'                        #print duplicate characters from list
d = defaultdict(int)
for i in string:
    d[i]+=1
print(d)

for k,v in d.items():
    if v > 1:
        print(k,end="")