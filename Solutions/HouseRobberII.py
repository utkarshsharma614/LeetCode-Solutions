class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=3:
            return(max(nums))
        
        def helper(dp):
            dp[1] = max(dp[0], dp[1])
            for i in range(2, len(dp)):
                dp[i] = max(dp[i-1], dp[i] + dp[i-2])
            
            return dp[-1]
        
        a = helper(nums[:len(nums)-1])
        b = helper(nums[1:])
        
        return max(a, b)