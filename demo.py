class student:
    def __init__(self,rno,name,age):
        self.rno=rno
        self.name=name
        self.age=age
    def display(self):
        print("roolno:",self.rno)
        print("name:",self.name)
        print("Age:",self.age)
objstd1=student(100,"Karthik",46)
objstd2=student(101,"Khasif",34)
print(objstd1.display())
print(objstd2.display())

