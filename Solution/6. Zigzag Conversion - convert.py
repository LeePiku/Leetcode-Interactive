class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Special case 
        if numRows == 1 or numRows >= len(s):
            return s

        # Input
        count = 0
        index = 0
        direction = 0
        data = [[] for row in range(numRows)]

        for char in s:
            data[index].append(char)

            # Adjust next turn index
            if direction == 0:
                index += 1
            else:
                index -= 1

            # Adjust next turn direction
            if index == 0:
                direction = 0 # Increment
            if index == numRows - 1:
                direction = 1 # Decrement
        
        # Output 
        for i in range(numRows):
            data[i] = "".join(data[i]) # Merge row
        return "".join(data) # Merge columns

        
