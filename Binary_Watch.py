import collections
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        time=[]
        for i in range(12):
            for j in range(60):
                b=bin(i<<6 | j)
                count=0
                for k in range(2,len(b)):
                    if b[k]=='1':
                        count=count+1
                if count==num:
                    s=str(i)
                    if j>=10:
                        s=s+":"+str(j)
                    else:
                        s=s+":0"+str(j)
                    time.append(s)
        return time
  
class Solution1(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """ 
        return ["%d:%02d" % (i,j) for i in range(12) for j in range(60) if (bin(i)+bin(j)).count('1')==num]
        
                
s=Solution1()
print s.readBinaryWatch(1)