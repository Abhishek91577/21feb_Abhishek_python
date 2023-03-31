"""write a python program to remove an empty tuples from list of tuples"""
l=[(),(),('',),('a','b'),('a','b','c','d')]
l=[t for t in l if t]
print(l)