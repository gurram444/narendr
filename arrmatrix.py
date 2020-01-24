from numpy import *
arr1=array([
    [1,2,3,4],[6,7,8,9]
])
#print(arr1)
#print(arr1.dtype)   # type of data
#print(arr1.ndim)  #number of dimensions
#print(arr1.shape)   # number of rows n columns
#print(arr1.size)
#arr2=arr1.flatten()    # two dimensions into single dimension
#print(arr2)
#arr3=arr2.reshape(3,4) # creating 3 dimension array using 2 dimension array
#print(arr3)
#arr4=arr1.reshape(2,2,3) # creating 2 dimension array in 2 dimension array
#print(arr4)
m =matrix('1 2 3 ;4 5 6; 7 8 9')
m1=matrix('1 2 3;4 5 6;7 8 9')
m2=matrix('1 2 3;4 5 6;7 8 9')
m3=m1+m2
m4=m1*m2
print(m3)
print(m4)
print(diagonal(m))
print(m.max)