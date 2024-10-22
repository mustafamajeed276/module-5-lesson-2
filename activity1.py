class IOSstring():
    def __init__(self):
        self.str1 = ""
    def getstring(self):
        self.str1 = input("enter a string in lower case : ")
    def printstring(self):
        print("result is : ", self.str1.upper())
str1 = IOSstring()
str1.getstring()
str1.printstring()