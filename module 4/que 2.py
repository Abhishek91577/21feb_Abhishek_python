"""write a python program to append text to a file and display the text"""
f=open("hello.txt","a")
stid=input("enter Id:")
stnm=input("enter Name:")
f.write(f"id{stid}\n Name{stnm}\n")