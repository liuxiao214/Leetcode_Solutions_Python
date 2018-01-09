a=6
def guess(num):
    if num>a:
        return -1
    elif num<a:
        return 1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        while True:
            mid=(high-low)/2+low
            if guess(mid)==1:
                low=mid+1
            elif guess(mid)==-1:
                high=mid-1
            else:
                return mid

s=Solution()
print s.guessNumber(10)
                
        