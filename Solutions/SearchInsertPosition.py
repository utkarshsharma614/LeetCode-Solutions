class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pos=0
        for i in range (0,len(nums)):
                if (nums[i]==target) :
                        return i
                if (nums[i]<target) :
                        pos=pos+1
        return pos