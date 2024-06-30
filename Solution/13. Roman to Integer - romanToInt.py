class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000        
        }
        s = s.replace('CD','CCCC').replace('CM','DCCCC')
        s = s.replace('XL','XXXX').replace('XC','LXXXX')
        s = s.replace('IV','IIII').replace('IX','VIIII')
        result = 0 
        for char in s:
            result += list_dict[char]
        return result 
        

            
        
