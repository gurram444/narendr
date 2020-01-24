def perfect(n):
    m=0
    for i in range(1,n):
        if n%i==0:
            m+=i
    if m==n:
        print(m,'is a perfect number')
    else:
        print('not perfect')
perfect(6)


i=1
while i<=100:
    m=0
    for j in range(1,i):
        if i%j==0:
            m+=j
    if m==i:
        print(i)
        i+=1
    else:
        i+=1
