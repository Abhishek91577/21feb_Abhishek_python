"""write a python function to check whether a nuber is perfect or not"""
def perfectnumber(n):
    sum=0
    for x in range(1,n):
        if n%x==0:
            sum+=x
            return sum==n
print(perfectnumber(6))