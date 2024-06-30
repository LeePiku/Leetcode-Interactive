class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Find smallest len strs
        min_strs = 201
        for i in strs:
            if len(i) < min_strs:
                min_strs = len(i)
        result = ''

        # Loop through smallest len
        for i in range(min_strs):
            check = strs[0][i]

            # Check with all strings index
            for j in range(len(strs)):
                if strs[j][i] == check:
                    pass
                else:
                    return result
            result += check

        return result
