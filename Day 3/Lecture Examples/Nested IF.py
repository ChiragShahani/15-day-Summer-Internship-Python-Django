#Nested If example
a=int(input('Enter Value fo a:'))
print('Value of a is', a)

if a >= 0:
    if a == 0:
        print(a ,'is zero')
    else:print(a , 'is Positive')

else:print(a, ' is negative')