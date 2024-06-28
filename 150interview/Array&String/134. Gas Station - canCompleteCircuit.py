class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        # To identify system validity
        net_gascost = 0
        # To identify valid loop
        current_gascost = 0
        idx = 0
        for i in range(len(gas)):
            net_gascost += gas[i] - cost[i]
            current_gascost += gas[i] - cost[i]
            if current_gascost < 0:
                current_gascost = 0 
                idx = i+1
        return idx if  net_gascost >= 0 else -1
