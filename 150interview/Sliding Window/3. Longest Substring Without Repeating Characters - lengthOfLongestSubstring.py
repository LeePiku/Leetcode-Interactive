class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = ''
        max_len = 0
        for char in s:
            # Repeating value handle
            if char in temp:
                max_len = max(len(temp),max_len)
                # Removing character before repeating value in current char
                temp = temp[temp.index(char)+1:] + char
            else:
                temp += char
        max_len = max(len(temp),max_len)
        return max_len
