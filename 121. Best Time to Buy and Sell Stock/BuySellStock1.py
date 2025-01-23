class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = 0
        profit = 0
        diff = 0
        for s in range(1,len(prices)):
            while prices[s] < prices[b]:
                b+=1
                
            diff = prices[s] - prices[b]
            profit = max(profit,diff)
        return profit


#Time : O(n) outer loop n times, inner at most n times
#Space: O(1) constant space
