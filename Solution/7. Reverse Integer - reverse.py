class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Set max integer threshold, instantiation
        max_int = 2 ** 31 - 1 # 2,147,483,647
        rev = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        # Reversing by multiplying moderators for positive cases
        while x != 0:
            if rev > max_int / 10:
                return 0
            rev = rev * 10 + x % 10 
            x = x // 10
        # Return result adjusting sign 
        return sign * rev
