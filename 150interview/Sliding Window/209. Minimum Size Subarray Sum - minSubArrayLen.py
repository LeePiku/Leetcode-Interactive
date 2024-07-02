class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Create accumulate nums array
        acc_nums = [0]
        for num in nums: acc_nums.append(acc_nums[-1]+num) 

        # Check feasibility
        if acc_nums[-1] < target: return 0
        else:
            # Init sliding window
            left = 0
            right = 1
            min_len = 100001
            # Sliding window when < target extend to right when > target pulling left
            while left < right and right < len(acc_nums):
                if acc_nums[right] - acc_nums[left] < target:
                    right += 1
                else:
                    min_len = min(min_len, right - left)
                    left += 1
            return min_len

