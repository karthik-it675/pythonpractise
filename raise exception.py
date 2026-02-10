try:
    a=int(input("enter a number:"))
    if a<0:
        raise ValueError("number cannot be zero")
    else:
        print(a)
except Exception as obj:
    print(obj)

