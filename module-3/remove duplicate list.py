"""write a python program to remove duplicates from list"""
lst=[2,3,7,7,7,2,2,8,9,10,8,10]
newlst=[]
for data in lst:
    if data not in newlst:
        newlst.append(data)
print(newlst)