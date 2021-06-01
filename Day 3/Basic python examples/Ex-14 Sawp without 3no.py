# Swap 2 number without help of 3 number
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
print('initial value ', a, ' & ', b)

a , b = b , a

print('after swapping value ', a, ' & ', b)