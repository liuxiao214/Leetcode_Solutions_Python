class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max=0
        buy=0
        for i in range(1,len(prices)):
            if prices[i]<prices[buy]:
                buy=i
            else:
                if (prices[i]-prices[buy])>max:
                    max=prices[i]-prices[buy]
        return max
    
s=Solution()
print s.maxProfit([7,1,5,3,6,4])