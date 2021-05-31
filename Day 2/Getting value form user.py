# Creating an empty list
list=[]

# Getting the number of elements as input from user with yhe help of input
n=int(input("Enter number of elements :"))

#Storing the value till the range given by user

for i in range(0,n):
    list2 = input("Enter value:")

    list.append(list2)#Adding the element
print(list)
