"""write a python program to read file line by line store it into variable"""
def fileread(fname):
    with open(fname,"r")as myfile:
        data=myfile.readlines()
        print(data)
        fileread('hello.txt')