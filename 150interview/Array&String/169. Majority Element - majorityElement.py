class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        max_index = nums[0]
        max_value = 0
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
                if dict[i] > max_value:
                    max_index = i
                    max_value = dict[i]
        return max_index
