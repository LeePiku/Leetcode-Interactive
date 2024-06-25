class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            if nums[i] == val: 
                nums[i] = 51
                result += 1 
        nums.sort()
        return len(nums) - result
        
