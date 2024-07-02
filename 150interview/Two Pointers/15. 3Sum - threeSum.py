class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        # 3 pointer method , i,  left and right 
        for i in range(len(nums)-2):
            # Check duplicate looping value
            if nums[i] <> nums[i-1] or i == 0:
                left = i+1
                right = len(nums)-1
                while left < right:
                    # Inc left when sum negative dec right when sum positive 
                    if nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        res = [nums[i],nums[left],nums[right]]
                        if res in result: pass 
                        else: result.append(res)
                        left += 1
                        right -= 1
        return result
