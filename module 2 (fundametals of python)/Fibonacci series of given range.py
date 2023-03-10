"""3) write a python program to get fibonacci series of given range."""
n=int(input("Enter nuber:"))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
   