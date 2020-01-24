import itertools
input1=['A','B','C','A']
input2=['B','C','A','D']
input3=['A','A','C','AC']
list=itertools.combinations(input1,2)
list1=itertools.permutations(input2,2)
list2=itertools.combinations_with_replacement(input3,2)
l=[i for i in list]
l1=[i for i in list1]
l2=[i for i in list2]
#print(l1)
z=[]
for i in l:
    z.append(i[0]+i[1])
print(z)
n=input("input string:")
if n in z:
    print('True')
else:
    print('False')


s=[]
for i in l1:
    s.append(i[0]+i[1])
print(s)
k=input("input sum:")
if k in s:
    print('True')
else:
    print('False')



j=[]
for i in l2:
    j.append(i[0]+i[1])
print(j)
a=input("input sum:")
if a in j:
    print('True')
else:
    print('False')

# m="".join(input1)
    #list=itertools.combinations(m,2)
    #j=[i for i in list]
    #print(j)


str='Narendra'
output=''
for i in str:
    if i.isupper():
        output+=(i.lower())
    else:
        output+=(i.upper())
print(output)
#print(''.join(output))

