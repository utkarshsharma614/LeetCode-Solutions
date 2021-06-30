class Solution:
    def __init__(self):
        self.res = set()
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        
        final = self.res
        return list(final)
        # final.sort()
        # return list(final for final,_ in itertools.groupby(final))
    
    def backtrack(self, nums, path):
        if not nums:
            # self.res.append(path)
            self.res.add(tuple(path))
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
    
    