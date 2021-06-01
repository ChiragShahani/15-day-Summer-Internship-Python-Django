# Check if the number is less than 100 and then check odd-even
a = int(input('Enter number:'))
if a < 100:
    if a % 2 == 0:
        print(a, 'is even number')
    else:
        print(a, 'is odd number')
elif a == 100:
    print(a, 'is equal than hundred')
else:
    print(a, 'is greater than hundred')

