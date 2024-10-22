class employee:
    def __init__(self):
        print("employee created")
    def __del__(self):
        print("destructer created! arrgh!")
def createobj():
    print("making object...")
    obj = employee()
    print("function end... yes that's all...")
    del obj
print("calling createobj function")
obj = createobj()
print("program(and party) ended...goodbye...")