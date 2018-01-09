def distributeCandies(candies):
    a = len(set(candies))
    b = len(candies)
    return min(a,b/2)
'''allen = len(candies)
        flag = []
        for i in range(allen):
            if candies[i] not in flag:
                flag.append(candies[i])
        kind = len(flag)
        if kind <= (allen/2):
            return kind
        else:
            return allen/2'''
print distributeCandies([1,1,2,2,3,3])