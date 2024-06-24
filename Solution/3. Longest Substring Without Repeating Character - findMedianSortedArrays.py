class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 2 Pointer Approach
        # Function Merge 2 List
        def merge(list1,list2):
            list = []
            i = 0
            j = 0
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    list.append(list1[i])
                    i += 1
                else:
                    list.append(list2[j])
                    j += 1
            while i < len(list1):
                list.append(list1[i])
                i += 1
            while j < len(list2):
                list.append(list2[j])
                j += 1
            return list

        # Merge 2 List
        sorted_list = merge(nums1,nums2)
        l = len(sorted_list)

        # Return median value
        if (l % 2) != 0:
            return float(sorted_list[(l-1)//2])
        else:
            return (sorted_list[l/2] + sorted_list[l/2-1])/2.0
        
