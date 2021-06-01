# Take 3 numbers and find greater number using Nested if else
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of b: '))
if a < b:
    if b < c:
        print(c, 'is greater than', a, '&', b)
    else:
        print(b, 'is greater than', a, '&', c)
elif b < c:
    if c < a:
        print(a, ' is greater than', b, '&', c)
    else:
        print(c, ' is greater than', a, '&', b)



