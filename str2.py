class s:
    def __init__(self,a):
        self.a=a
    def reverse(self):
        c=self.a.split()
        b=' '.join(reversed(c))
        print(b)
obj=s('narendra naresh')
obj.reverse()


s='narendra'               # removing duplicates
o=''.join(set(s))
print(o)


l=[2,5,3,6,85,3,4,5,8,9,4,5,7]             # display duplicate elements in list
m=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i]==l[j]) and (l[i] not in m):
            m.append(l[i])

print(m)