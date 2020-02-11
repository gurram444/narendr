l=[]                          # print nums that are divisible by 7 and not multiples of 5
for i in range(1,20):
    if (i%7==0) and (i%5!=0):
        l.append(i)
print(l)

import collections             # count characters repeated in string
str='narendranareshmanideep'
d=collections.defaultdict(int)
for i in str:
    d[i]+=1
print(d)
for j,k in d.items():
    if k>1:
        print(j,k)


list=[5,3,4,2,9,6,7,8,10]       #getting last n elements from list
n=4
res=list[-n:]
print(res)


lst=[4,2,3,2,5,2,1,3]             # find most frequent element in list
counter=0
num=lst[0]
for i in lst:
    cur=lst.count(i)
    if cur>counter:
        counter=cur
        num=i
print(num)

list1=[78,5,7,88,5,98,122,53,65,887,899,43,55]      # sorting list
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)


l1=[-1,-2,-3,4,-5,8]                      #convert -ve num into positive numbers
x=[abs(i) for i in l1]
print(x)