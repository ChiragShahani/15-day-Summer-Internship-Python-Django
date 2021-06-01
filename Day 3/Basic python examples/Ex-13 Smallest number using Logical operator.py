# Take 3 numbers and find smallest number using logical operator
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of b: '))
if a < b and a < c:
    print(a, ' is smallest than ', b, '&', c)
elif b < a and b < c:
    print(b, ' is smallest than ', a, '&', c)
elif c < a and c < b:
    print(c, ' is smallest than', a, '&', b)
