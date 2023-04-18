"""write a python program to read first n lines of a file"""
n=int(input ("\n\t\t Enter lines to read:"))
f1=open("hello.txt",'r')
for i in range(n):
    print(f1.readline())