"""write a python program to sum of the first n postive integers."""
from re import I


n=int(input("Enter nuber you want"))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print("sum=",sum)


