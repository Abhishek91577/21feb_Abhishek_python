"""write function that takes two lists and returns if they at least one coomon member"""
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
for x in l1:
    for y in l2:
        if x==y:
            print("True")