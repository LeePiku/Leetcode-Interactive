class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 pointer approach 
        char_table = {}
        pointer_1 = -1
        pointer_2 = 0
        result = 0

        for char in s:
            pointer_1 += 1
            if char not in char_table:
                char_table[char] = 0
            char_table[char] += 1 

            # When char count reach 2 , using pointer to eliminate char count to repeated value 
            while char_table[char] > 1: 
                char_table[s[pointer_2]] -= 1
                pointer_2 += 1  
            result = max(result,pointer_1 - pointer_2 +1)
        return result
