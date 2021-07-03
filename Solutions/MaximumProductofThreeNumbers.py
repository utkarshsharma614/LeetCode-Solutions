class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        
        nums.sort()
        
        prod1 = nums[-1] * nums[-2] * nums[-3]
        
        prod2 = 0
        
        if nums[0] < 0 and nums[1] < 0:
            prod2 = nums[0] * nums[1] * nums[-1]
        
        return max(prod1, prod2)