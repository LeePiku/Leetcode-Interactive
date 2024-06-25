class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup = 102
        count = 0
        for i in range(len(nums)):
            if nums[i] == dup:
                nums[i] = 101
            else:
                dup = nums[i]
                count += 1 
        nums.sort()
        return count
