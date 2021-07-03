class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = nums[:]
        num.sort()
        
        index = len(nums) - 1
        
        for i in range(1, len(nums), 2):
            nums[i] = num[index]
            index -= 1
        
        for i in range(0, len(nums), 2):
            nums[i] = num[index]
            index -= 1
        
        