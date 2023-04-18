"""write a python program to read last n lines of a file."""
n=int(input("Enter n LInes:"))
f=open("hello.txt",'r')
for n in (f.readlines()):