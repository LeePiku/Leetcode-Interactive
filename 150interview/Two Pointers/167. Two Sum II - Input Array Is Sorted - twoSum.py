class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,j in enumerate(numbers):
            if target-j in dict:
                return [dict[target-j]+1,i+1]
            if j not in dict:
                dict[j] = i
