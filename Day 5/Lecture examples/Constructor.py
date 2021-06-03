# Default costructor & parameterized constructor
class Demo:
    def myFunction(self):
        print("This is class function")

    def show(self, name):
        print("Parameter is ", name)

    '''def __init__(self):
        print("This is default constructor")'''

    def __init__(self, surname):
        print("This is constructor")
        print("Surname is ", surname)

d1 = Demo("Shahani")
d1.myFunction()
d1.show('Chirag')