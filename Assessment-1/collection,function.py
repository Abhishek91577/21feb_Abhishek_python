print("WELCOME TO PYTHON E-NOTE")
print("press 1 for generate note")
print("press 2 for view Note")
print("press 4 exit")
c=int(input("Enter your choice :"))
f1=open("test.txt",'a')
if c==1:
    def enote():
        gn=input("Enter python generator :")
        ti=input("Enter python e-note title :")
        oy=input("Enter e-note content :")
        f1.write(f"gname{gn}\n enotetitle{ti}\n enotecontent{oy}\n")
        n=int(input("Enter number of notes :"))
        for i in range(n):
            enote()
    enote()      
elif c==2:
    f1=open("test.txt",'r+')
    def vnote():
        gn=input("Enter python generator:")
        ti=input("Enter python e-note title:")
        oy=input("Enter e-note content")
        f1.write(f"genratorName{gn}\n EnoteTitle{ti}\n Enotecontent{oy}\n")
        print(f1.read())
    vnote()
else:
    print("EXIT")    


