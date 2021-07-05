class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            currSum, maxSum = nums[0], nums[0]
            for num in nums[1:]:
                currSum = max(currSum + num, num)
                maxSum = max(maxSum, currSum)
            return maxSum
        
        k = kadane(nums)
        
        cs = 0
        
        for i in range(len(nums)):
            cs += nums[i]
            nums[i] *= -1
        cs += kadane(nums)
        
        if cs > k and cs != 0:
            return cs
        
        else:
            return k