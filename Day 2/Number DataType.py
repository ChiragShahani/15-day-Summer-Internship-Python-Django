#Number DataType
'''Number dataType stores numeric values'''
"""int, float, complex numbers coms under number datatype"""
n1=20
print(n1, "is type of", type(n1))
n2=20.5
print(n2, "is type of", type(n2))
print(n2, "Is complex number?", isinstance(n2,int))
n3=20+20.5j
print(n3, "is type of", type(n3))
print(n3, "Is complex number", isinstance(n3,complex))