n=int(input("enter number:"))       #find powers of number
i=int(input("power of number:"))
j=n**i
print(j)


sentense='narendrabsccomputers'      #find all vowels and their count in sentense
vowel=['a','e','i','o','u']
for i in vowel:
    if i in sentense:
        print(i,sentense.count(i))


list=[2,3,4,1,4,6,9,12,23,56,76,97]     #remove every third element from list and display number
for i in range(len(list)-1):
     if i in[2,4,6,8]:
         print(list[i],list.remove(list[i]))
print(list)


def count_currency(amount):                   #find currency count
    notes=[2000,500,200,100,50,20,10,5,1]
    count=[0,0,0,0,0,0,0,0,0]
    print('count currency---->')
    for i,j in zip(notes,count):
        if amount>=i:
            j=amount//i
            amount=amount-j*i
            print(i,':',j)
amount=868
count_currency(amount)