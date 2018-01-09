import collections
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0 or len(points)==1 or len(points)==2:
            return 0
        sum=0      
        for i in range(len(points)):
            dist={}
            for j in range(len(points)):
                temp=(points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
                dist[temp]=1+dist.get(temp, 0)
            for k in dist:
                sum=sum+dist[k]*(dist[k]-1)
        return sum
    
s=Solution()
lists=[[0,0],[1,0],[2,0]]
print s.numberOfBoomerangs(lists)