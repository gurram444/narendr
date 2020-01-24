pos=-1                    #linear search
def search(list,n):
    i=0
    while i<=len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    return False

list=[3,5,4,7,9,6]
n=10
if search(list,n):
    print('found at',pos+1)
else:
    print('not found')






