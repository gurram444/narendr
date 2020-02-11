pos=-1                    #linear search
def search(list,n):
   l=0
   u=len(list)-1
   while l<=u:
       mid=(l+u)//2
       if list[mid]==n:
           globals()['pos']= mid
           return True
       else:
           if list[mid]<n:
               l=mid+1
           else:
               u=mid-1
   return False

list=[3,5,4,7,9,6,43,41,53,452]
n=452
if search(list,n):
    print('found at',pos+1)
else:
    print('not found')


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("Element is present at index:", result)
else:
    print("Element is not present in array")






