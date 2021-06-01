# Print square of a number if it is less than 10
a = int(input('Enter number: '))
if a < 10:
    sq = a * a
    print(sq, 'is square of', a)
elif a == 100:
    print(a, 'is equal to 10')
else:
    print(a, 'is greater than 10')


