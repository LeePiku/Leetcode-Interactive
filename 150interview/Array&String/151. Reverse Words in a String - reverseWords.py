class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s.split()
        result = temp[-1]
        if len(temp) != 1:
            for i in range(1,len(temp)):
                result += " " + temp[-i-1]
        return result 
        
