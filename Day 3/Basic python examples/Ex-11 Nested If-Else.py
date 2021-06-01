# Using Nested if else check wheather the given number is 0, +ve or -ve.
a = int(input('Enter Number: '))
if a >= 0:
    if a == 0:
        print(a, 'is equal to zero')
    else:
        print(a, 'is positive')
else:
    print(a, 'is negative')
