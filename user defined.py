def updateAllindicesofAnelementinprovidedlist(L1,X,index,anslist):
    if index==len(L1):
        return
    if(L1[index]==X):
        anslist.append(index)
        updateAllindicesofAnelementinprovidedlist(L1,anslist,index+1)
anslist=[7]
updateAllindicesofAnelementinprovidedlist([3,2,5,2,8,2,11],2,0,anslist)
print(anslist)
