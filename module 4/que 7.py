"""write a python program to write a list to a file"""
l1=["apple","banana","graphs","orange"]
f1=open("demo.txt",'a')
f1.writelines(l1)
print("File created")