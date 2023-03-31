"""write a python script to check  if key already exists in a dictionary"""
d={1:10,2:20,3:30,4:40,5:50}
def is_key(x):
    if x in d:
        print("key is exists")
is_key(5)
is_key(7)

