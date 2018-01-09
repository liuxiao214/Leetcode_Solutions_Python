def findContentChildren(g, s):
    sum = 0
    g.sort()
    s.sort()
    t = 0
    for i in range(len(g)):
        for j in range(t,len(s)):
            if g[i]<=s[j]:
                sum = sum + 1
                t = j+1
                break
    return sum
print findContentChildren([1,2,3],[1,2])
    
    