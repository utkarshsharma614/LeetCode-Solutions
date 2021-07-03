class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        if not any(map(bool, nums)):
            return '0'
        
        nums = list(map(str, nums))
        
        if len(nums) <= 1:
            return "".join(nums)
        
        def compare(i, j):
            return int(nums[i] + nums[j]) > int(nums[j] + nums[i])
        
        for i in range(len(nums) - 1):
            j = i + 1
            while i < len(nums) and j < len(nums):
                if compare(i, j):
                    pass
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                
                j += 1
        
        return "".join(nums)