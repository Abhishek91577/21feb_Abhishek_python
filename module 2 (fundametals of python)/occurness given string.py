"""program to count number of times a character occurs in given string"""
string=input("enter the any string:")
c=input("check character to check frequency:")
count=0
for i in string:
    if i==c:
        count+1
print(c,"occurs",count"times(s))