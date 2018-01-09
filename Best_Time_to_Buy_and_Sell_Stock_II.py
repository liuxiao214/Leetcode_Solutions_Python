class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        buy=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1] and i==len(prices)-1:
                profit = profit + prices[i] - prices[buy]
            if prices[i]<=prices[i-1]:
                profit = profit + prices[i-1] - prices[buy]
                buy=i
        return profit
    
s = Solution()
a=[1,9,6,9,1,7,1,1,5,9,9,9]
print s.maxProfit(a)
        