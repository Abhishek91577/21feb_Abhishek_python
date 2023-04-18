"""write a python program to find the longest words."""
def longestword(filename):
     with open (filename,'r') as infile:
         words=infile.read().split()
         max_len=len(max(words,key=len))
         return[word for word in words]
         if len(word)==max_len:
        print(longestword("demo.txt"))