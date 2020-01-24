import itertools        #find list combinations and find max of sublist
list=[2,3,5,9,7,8,1]
list=itertools.combinations(list,3)
list1=[i for i in list]
print(list1)
res=max(list1,key=sum)
print('sum of sublist is:',res,':',sum(res))



number=int(input('enter number:'))      #reversing negative number
str=str(number)
l=str[0]+str[:0:-1]
print(int(l))


n=123                                   #sum of number
sum=0
while n>0:
    remainder=n%10
    sum+=remainder
    n=n//10
print(sum)


number=int(input('enter number:'))           #palindrome number
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


number=int(input("enter number"))             #armstrong number
temp=number
sum=0
while number>0:
    rem=number%10
    sum+=rem*rem*rem
    number=number//10
if temp==sum:
    print("given number is armstrong",sum)
else:
    print("given number not a armstrong")


number=int(input('enter number:'))            #reverse of number
reverse=0
while number>0:
    rem=number%10
    reverse=(reverse*10)+rem
    number=number//10
print("reverse of number is:",reverse)