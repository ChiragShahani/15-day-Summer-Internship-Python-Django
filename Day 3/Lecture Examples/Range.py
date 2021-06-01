# Range function example
for i in range(5):
    print('First range is:', i)
for i in range(0, 5):
    print('Second range is:', i)
for i in range(1, 5, 2):
    print('Third range is:', i)

# len() and range() fusion example
list1 = [22, 44, "Chirag", "Shahani"]
for i in range(len(list1)):
    print('Range of l1 is:', list1[i])
else:
    print("No elements left.")