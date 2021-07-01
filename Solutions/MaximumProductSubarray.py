class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        arr = nums[::-1]
        
        for index in range(1, len(nums)):
            if nums[index-1] != 0:
                nums[index] *= nums[index - 1]
            
            if arr[index-1] != 0:
                arr[index] *= arr[index - 1]
        
        return max(nums + arr)