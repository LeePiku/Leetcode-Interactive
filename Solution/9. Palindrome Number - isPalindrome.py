class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        s = x

        # Special handling
        if x < 0:
            return False

        # Find reverse int
        while s != 0 :
            reverse = reverse * 10 + s % 10 
            s = s // 10
        
        # Check condition
        if x == reverse:
            return True
        else:
            return False
