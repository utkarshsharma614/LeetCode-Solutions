class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.dp = [-1] * (target+1)
        return self.solve(nums, target)
    
    def solve(self, nums, target):
        if target == 0:
            return 1
        
        if self.dp[target]!=-1:
            return self.dp[target]
        
        res = 0
        for i in nums:
            if target>=i:
                res += self.solve(nums, target -i)
        self.dp[target] = res
        return res
        