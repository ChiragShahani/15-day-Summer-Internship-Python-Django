#List DataType
list1 = [1,2,3,"Four",5,6,"seven"]
print(list1,type(list1) )

print("list1[2] =", list1[2])
print("list1[0: 5] =", list1[0:5])
print("list1[3:] =", list1[3:])
# List are mutable, value can be changed
list1[0] = 11
print(list1)