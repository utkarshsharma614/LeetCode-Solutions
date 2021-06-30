class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        if n==0 :
            return n
        while val in nums:
            nums.remove(val)
        return len(nums)
            