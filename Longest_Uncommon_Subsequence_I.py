def findLUSlength(a, b):
    if a==b:
        return -1
    if len(a)>len(b):
        return len(a)
    else:
        return len(b)
    
print findLUSlength("dggsdg","sds")