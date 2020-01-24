num=int(input('enter number'))
if num>1:
    for i in range(2,num//2):
        if(num%i==0):
            print(num,'number is not prime')
            break
    else:
        print('number is prime number')
else:
    print('number is not prime number')





n=int(input('enter range:'))
for num in range(2,n+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
          print(num,end=",")

