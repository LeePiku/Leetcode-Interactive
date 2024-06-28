class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        right = 1
        answer = [1]
        # Forward loop
        for i in range(1,l):
            answer.append(answer[i-1]*nums[i-1]) 
        # Backward loop
        for i in range(1,l+1):
            answer[-i] =  answer[-i] * right
            right = right * nums[-i] 
 
        return answer
