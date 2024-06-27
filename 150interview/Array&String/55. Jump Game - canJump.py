class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest = 1
        for i in range(len(nums)):
            if i+1 <= furthest: 
                if (i+1+nums[i] > furthest):
                    furthest = i+1+nums[i]
        return furthest >= len(nums)
            
