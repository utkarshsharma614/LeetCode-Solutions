class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.cache=set()
        def dfs(target, nums):
            if target < 0:
                return False
            if target == 0:
                return True
            if target in self.cache:
                return False
            
            self.cache.add(target)
            
            for index, num in enumerate(nums):
                if dfs(target-num, nums[index+1:]) or dfs(target, nums[index+1:]):
                    return True
            return False
        
        sum_nums = sum(nums)
        if sum_nums % 2 !=0:
            return False
        
        return dfs(sum_nums // 2, nums)