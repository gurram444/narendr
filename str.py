str = 'cold'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)

#character count
print('len(str) = ', len(str))

d={'name':'nari','phone':83744,'place':'tpt'}
enumerate=list(enumerate(d))
print(enumerate)

st="narendra"    #1 reverse of string
print(st[::-1])

name='narendra'  #2 reverse of string
reverse=reversed(name)
output=''.join(reverse)
print(output)

def reverse(s):    #3 reverse of string
    output=''
    for i in range(len(s)-1,-1,-1):
        output +=s[i]
    return output
s=input('enter string')
output=reverse(s)
print(output)


def scrolling_text(text):
    b = len(text)
    c=[ text[i:]+text[:i] for i in range (b)]
    d=[i.upper() for i in c]
    print(d)

scrolling_text('codewars')