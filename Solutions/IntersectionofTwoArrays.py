class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        for i in nums1:
            set1.add(i)
        
        intersection = set()
        for i in nums2:
            if i in set1:
                intersection.add(i)
        
        return (list(intersection))