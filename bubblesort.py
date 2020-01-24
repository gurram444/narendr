
def sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]


nums=[4,7,8,2,3,9]
sort(nums)
print(nums)


def sort(nums):                                  #selectionsort
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        #print(nums)
nums=[6,5,7,2,4,9]
sort(nums)
print(nums)
