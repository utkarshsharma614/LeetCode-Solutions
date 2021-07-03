class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        count_zero = {}
        for i in nums1:
            for j in nums2:
                s = (i + j)
                if s in count_zero:
                    count_zero[s] += 1
                else:
                    count_zero[s] = 1
        for i in nums3:
            for j in nums4:
                target = 0 - (i + j)
                if target in count_zero:
                    count += count_zero[target]
        return count