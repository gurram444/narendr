number=121         #palindrome number
temp=number
reverse=0
while number>0:
    remainder=number%10
    reverse=reverse*10+remainder
    number=number//10

if reverse==temp:
    print("given number is palindrome",reverse)
else:
    print("given number is not palindrome",reverse)