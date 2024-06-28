class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        temp = [1] * l
        
        # Forward
        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                temp[i] += temp [i-1]
        # Backward
        candies = temp[-1]
        pre = 1 # Counting var
        for i in range(1,l):
            # Check backward
            if ratings[-i] < ratings[-i-1]:
                pre += 1
            else:
                pre = 1
            # Finalize candies value
            candies += max(pre,temp[-i-1])
        return candies
