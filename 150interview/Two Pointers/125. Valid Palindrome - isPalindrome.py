class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join([i for i in s if i.isalnum()])
        if len(s) % 2 == 0:
            left = len(s) // 2 - 1
            right = left + 1
        else:
            left = right = len(s) // 2 
        while right < len(s):
            if s[left] != s[right]:
                return False
            else:
                left -= 1
                right += 1
        return True

        
