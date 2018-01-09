class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True


class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0):
            return False
        xt=x
        y=0
        while x>0:
            y=y*10+x%10
            x=x/10
        return xt==y
  
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0):
            return False
        y=0
        while x>y:
            y=y*10+x%10
            x=x/10
        return x==y or x==(y/10)
      
s=Solution2()
print s.isPalindrome(1221)