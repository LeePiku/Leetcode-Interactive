import random
class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.idx_map = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Check if val in
        if val in self.idx_map:
            return False
        
        self.list.append(val)
        self.idx_map[val] = len(self.list) - 1
        return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Check if val in
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        self.list[idx] = self.list[-1]
        self.idx_map[self.list[-1]] = idx
        del self.idx_map[val]
        self.list.pop()
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
