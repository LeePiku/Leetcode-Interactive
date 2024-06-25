class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []

        for char in s:
            # Add first character 
            if len(result) == 0:
                if char == '-' or char == '+' or char.isnumeric(): # Add first char
                    result.append(char)
                elif char == ' ': # Pass whitespace
                    continue
                else: # Break special char
                    break
            else:
                if char.isnumeric(): # Add number
                    result.append(char)
                else: 
                    break

        # Special case handling
        if len(result) == 0:
            return 0
        elif len(result) == 1 and (result[0] == "-" or result[0] == "+"):
            return 0
        else:
            result = int("".join(result)) # Convert to integer

        # Rounding within 32 bit integer range
        if result >= 0:
            return min(result,2**31 - 1)
        else:
            return max(result,-2**31)
            
            
        
