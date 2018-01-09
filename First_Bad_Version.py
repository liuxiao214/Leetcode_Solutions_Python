# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=0
        high=n
        mid=0
        while high-low>1:
            mid=low+(high-low)/2
            if isBadVersion(mid)==True:
                high=mid
            else:
                low=mid
        return high


class Solution1(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1
        high=n
        mid=0
        while low<high:
            mid=low+(high-low)/2
            if isBadVersion(mid)==True:
                high=mid
            else:
                low=mid+1
        return high
        