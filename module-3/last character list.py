"""write python program to count the number of strings where the string length 2 or  more and the first and last character are same list"""
words=["abc","xyz","aba","1221","343","def"]
count=0
for w in words:
    if len(w)>1 and w[0]==w[-1]:
        count+=1
print(count)