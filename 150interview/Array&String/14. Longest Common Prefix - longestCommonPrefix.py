class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Create list of len strs
        l = [len(i) for i in strs]
        result = ''

        # Loop through smallest len
        for i in range(min(l)):
            check = strs[0][i]

            # Check with all strings index
            for j in range(len(strs)):
                if strs[j][i] == check:
                    pass
                else:
                    return result
            result += check
            
        return result
