class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h = len(height) 
        peak = 0 
        water = [0] * len(height) 

        # Fill water from left
        for i in range(h):
            if height[i] > peak:
                peak = height[i]
            water[i] = peak - height[i]

        w_sum = 0
        peak = 0 
        # Fill water from right
        for j in range(h):
            if height[-j-1] > peak:
                peak = height[-j-1]
            w_sum += min(water[-j-1], peak - height[-j-1])
        
        return w_sum
            

        
