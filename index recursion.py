def firstindexofanelement(l1,x):
    if(len(l1)==0):
        return -1
    if(l1[0]==x):
        return 0
    ansFromRecurssion=firstindexofanelement(l1[1:],x)
    if(ansFromRecurssion==-1):
        return ansFromRecurssion
    else:
        return ansFromRecurssion+1
print(firstindexofanelement([5,6,7,8],10))