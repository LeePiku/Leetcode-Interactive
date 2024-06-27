class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = 0
        citations = sorted(citations,reverse=True)
        for i in range(len(citations)):
            if i < citations[i]: 
                count += 1
        return count
