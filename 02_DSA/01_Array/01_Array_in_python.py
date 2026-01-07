import array as arr

# myarr = arr.array ('i',[1,5,6,7,7]);
# myList= [1,3,"farman","kaif","suhail",4.5,7.5,"@"]

# # for i in range(0,5):
# #     print(myarr[i])

# # print(" ")


# # for i in range(0,len(myarr)):
# #     print(myarr[i])

# # print(" ")

# # for i in myarr:
# #     print(i)

# # print(myarr)
# # print(myList)

# # for i in myList:
# #     print(i)


# # Reversing an array 

# # myarr.reverse()
# # myList.reverse()


# # print(myarr)
# # inserting element 

# myarr.insert(3,500)
# myarr.append(100)
# myList.insert(3,500)
# myList.append(100)

# # copy Array 

# copyArr= arr.array(myarr.typecode,[])




# for i in myarr:
#     copyArr.append(i)


# print(myarr)

# print(copyArr)

# print(copyArr==myarr)



# # copyArr2=myarr # shallow copy 

# # print(copyArr2)

# # print(copyArr==myarr)
# # print(copyArr==copyArr2)

# # copyArr2.pop()

# # print(copyArr2)
# # print(myarr)

# # myarr.pop()

# # print(copyArr2)
# # print(myarr)
# # print(copyArr)

# # print(copyArr2==myarr)

# # Alternate method 

# copyArr3=arr.array(myarr.typecode,(i for i in myarr)) # Deep copy 

# print(copyArr3)

# # copyArr3.pop()
# copyArr3.remove(7)

# print(type(copyArr3))
# print(myarr)
# print(copyArr3)

# print(type(myList))

# for i in  copyArr3:
#     print(i)

# -----------------------------------------------------------------

# myArr=arr.array('i',[10,20,30,50,70,80,100])
# print(myArr)
# # myArr.reverse()
# # print(myArr)

# # ReversedArray=myArr # Shallow copy


# ReversedArray=arr.array(myArr.typecode,[])

# for i in range(len(myArr)-1,0,-1):
#     ReversedArray.append(myArr[i])


# print(ReversedArray)
# print(myArr)

# # -------------------------------------------------
# # Sclicing 

# # newArr=myArr[2:]
# # newArr=myArr[-3:-1]
# # newArr=myArr[0:-3]

# newArr = myArr[::-1]

# print(newArr)
# print(myArr)
# print(ReversedArray)


# # --------------------------------------------
# # UserInput 

# # User_Array= arr.array('i',[])
# # user_input_len= int(input("Enter len  of Array : "))

# # # print(type(user_input))

# # for i in range(0,user_input_len):
# #     User_Array.append(int(input("Enter number : ")))



# # for i in User_Array:
# #     print(i , end=" " )

# # print("")



# # print(User_Array)

# -----------------------------------------------------

Another_Array= arr.array('i',[23,67,89,87,67,56,45])

i= Another_Array.index(23)
print(i)
print(Another_Array)