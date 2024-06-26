class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                sum += (prices[i+1]-prices[i])
        return sum
