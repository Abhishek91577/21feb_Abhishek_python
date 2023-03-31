"""write a python program to map two lists into a dictionary"""
keys=['red','green','blue']
values=['#ff0000','#008000','#000ff']
color=dict(zip(keys,values))
print(color)