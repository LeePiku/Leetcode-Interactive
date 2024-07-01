class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        idx = 0 
        for word in t:
            if idx < len(s) and s[idx] == word:
                idx += 1 
        return True if idx == len(s) else False
