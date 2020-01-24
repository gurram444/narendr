for row in range(7):            # A pattern
    for col in range(5):
        if (row==0) and (col in{1,2,3}):
            print("*",end=" ")
        elif (row in{1,3,4,5,6}) and col in{0,4}:
            print("*",end=" ")
        elif row==2:
            print("*",end=" ")
        else:
            print(' ', end=' ')
    print()


for row in range(7):             # N pattern
      for col in range(5):
          if col in{0,4} and row not in {1,3,5}:
              print("*",end=" ")
          elif row==1 and col in{0,1,4}:
              print('*', end=" ")
          elif row==3 and col in{0,2,4}:
              print("*",end=" ")
          elif row==5 and col in{0,3,4}:
              print('*',end=' ')
          else:
              print(' ', end=' ')
      print()

n=int(input('enter value:'))
for i in range(n+1):
    for j in range(i):
        print(i,end='')
    print()

for i in range(n+1):
    print(i*'*')

for i in range(1,n):
    print(str(i)*i)

print("hello hari")