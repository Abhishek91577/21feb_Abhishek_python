"""write  python program to read a file line by line and store it into list"""
l1=["python","java","php","Angular"]
file=open("demo.txt",'a')
file.writelines(l1)
print("file created")
file.close()