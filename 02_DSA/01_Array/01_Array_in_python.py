from array import *

# Array using Array module 

arr1=array('i', [1,2,3,4,5])

for i in arr1:
    print(i, end=" ")

print()

print(arr1)


# Reverse Array 

new_arr=array('i',[1,2,3,4,5,6,7,8,9,10])
another_array=array('i',[1,2,3,4,5,6,7,8,9,10])
print("Array before reverse",new_arr)
Third_Array=new_arr
i=0
j=len(new_arr)-1
while(i<j):
    temp=new_arr[i]
    new_arr[i]=new_arr[j]
    new_arr[j]=temp
    i=i+1
    j=j-1


print("Array after reverse",new_arr)


Third_Array.reverse()
print(Third_Array)
print(new_arr)
print(another_array)



# Deep copy shallow copy 

print(new_arr is Third_Array)
print(new_arr is another_array)
# for i in new_arr:
#     print(i, end=" ")