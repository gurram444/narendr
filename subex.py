l=[2,5,1,3,4]    # min &max of sum of list
l1=sorted(l)
print(l1)
k=0
for i in range(4):
    k+=l1[i]
j=0
#l2=l1[::-1]
for i in range(1,5):
    j+=l1[-i]
print(k,j)


def substring(s):       # string palindrome
    l=len(s)
    for end in range(l,0,-1):
        for i in range(l-end+1):
            yield s[i: i+end]

def palindrome(s):
    return s==s[::-1]
def question(a):
    for l in substring(a):
        if palindrome(l):
            return l
print(question('afternoonmomdadmalayalam'))

