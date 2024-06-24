class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Set default result
        result = s[0]

        # Find palindrome string
        def find_pal(l,r):
            while l > 0 and r < len(s) -1 and s[l-1] == s[r+1]:    
                    l -= 1
                    r += 1
            return s[l:r+1]

        # Loop through string indexes
        for index in range(len(s)-1):
            # Case odd sub string
            sub_1 = find_pal(index,index)
            if len(sub_1)>len(result):
                result = sub_1
              
            # Case even sub string
            if s[index] == s[index+1]:
                sub_2 = find_pal(index,index+1)
                if len(sub_2)>len(result):
                    result = sub_2
        
        return result
