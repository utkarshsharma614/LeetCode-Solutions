class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <=0 or nums[i] > len(nums) + 1:
                nums[i] = len(nums) + 1
        
        for num in nums:
            num = abs(num)
            if num - 1 < len(nums) and nums[num - 1] > 0:
                nums[num - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1