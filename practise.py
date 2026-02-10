list=[2,3,4,56,8]
try:
    index=list.index(9)
    print(index)
except ValueError:
    print("element is not in list")