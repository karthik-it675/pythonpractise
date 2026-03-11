class demo:
    def __init__(self):
        print("the address of self is:",id(self))
obj1=demo()
obj2=demo()
print(id(obj2))

