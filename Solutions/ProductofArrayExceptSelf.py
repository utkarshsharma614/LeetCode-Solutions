class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        
        for i in range(len(nums)-1, 0, -1):
            result.append(result[-1] * nums[i])
        
        result = result[::-1]
        
        left = 1
        
        for i in range(len(nums)):
            result[i] = result[i] * left
            left = left * nums[i]
        
        return result