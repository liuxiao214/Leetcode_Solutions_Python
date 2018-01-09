class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        hex=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        count=0
        hnum=""
        while(num and count<8):
            hnum=hex[0b1111 and (num%16)]+hnum
            num=num>>4
            count+=1
        return hnum
   
class Solution1(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return ''.join('0123456789abcdef'[ (num>>4*i) & 15 ] for i in range(8) )[::-1].lstrip('0') or '0'
        
    
s=Solution1()
print s.toHex(0)