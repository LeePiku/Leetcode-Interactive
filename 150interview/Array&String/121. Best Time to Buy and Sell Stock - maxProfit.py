class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 10001
        result = 0
        for i in prices:
            if i < min:
                min = i
            else:
                if i-min > result:
                    result = i-min
        return result
            
            
            
            
