class UpperString():
    def __init__(self):
        self.input_str = " "

    def getString(self):
        self.input_str = input()
    
    def printString(self):
        print(self.input_str.upper())

p1 = UpperString()
p1.getString()
p1.printString()