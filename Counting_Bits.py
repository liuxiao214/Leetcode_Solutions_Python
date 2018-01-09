class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def getbit(num):
            count=0
            while num>0:
                if num%2==1:
                    count+=1
                num=num/2
            return count
        bits=[0]*(num+1)
        for i in range(1,num+1):
            bits[i]=getbit(i)
        return bits

class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits=[0]*(num+1)
        for i in range(1,num+1):
            bits[i]=bits[(i-1)&i]+1
        return bits
    
class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits=[0]
        j=1
        while j<=num:
            i=0
            n=len(bits)
            while i<n and j<=num:
                bits.append(bits[i]+1)
                i+=1
                j+=1
        return bits

class Solution3(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits=[0]*(num+1)
        for i in range(1,num+1):
            bits[i]=bits[i/2]+i%2
        return bits

class Solution4(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits=[0]*(num+1)
        for i in range(1,num+1):
            bits[i]=bits[i>>1]+i%2
        return bits
    
s=Solution4()
bits=s.countBits(16)
print bits