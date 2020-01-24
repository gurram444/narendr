x='radar'       #string palindrome
y=''
for i in x:
    y=i+y
    if x==y:
        print('yes')


def ispalindrome(s):
    rev=''.join(reversed(s))
    if rev==s:
        return True
    return False
s='malayala'
ans=ispalindrome(s)
if ans:
    print('yes')
else:
    print('no')


def palindrome(str):
    output=str[::-1]
    return output
str='malayala'
obj=palindrome(str)
if obj==str:
    print('ispalindrome')
else:
    print('not palindrome')