class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()        
        maxidx=0
        s=0
        for i in range(len(houses)):
            temp=abs(heaters[s]-houses[i])
            for j in range(s+1,len(heaters)):
                if heaters[j]==houses[i]:
                    temp=0
                    break
                elif heaters[j]<houses[i]:
                    if houses[i]-heaters[j]<temp:
                        temp=houses[i]-heaters[j]
                    s=j
                else:
                    if heaters[j]-houses[i]<temp:
                        temp=heaters[j]-houses[i]
                    break
            if temp>maxidx:
                maxidx=temp
        return maxidx

class Solution1(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        maxidx=0
        index=0
        for i in range(len(houses)):
            while index+1<len(heaters) and (abs(heaters[index+1]-houses[i])<=abs(heaters[index]-houses[i])):
                index+=1
            maxidx=max(maxidx,abs(heaters[index]-houses[i]))
        return maxidx
        
    
s=Solution1()
'''
houses=[101027544, 144108930, 282475249, 457850878, 458777923, 470211272, 622650073, 984943658]
heaters=[16531729, 74243042, 114807987, 115438165, 137522503, 143542612, 441282327, 784484492, 823378840, 823564440]
'''
houses=[282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters=[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

print s.findRadius(houses, heaters)
                        

