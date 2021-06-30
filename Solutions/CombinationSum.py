class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.res
    
    def backtrack(self, path, target, index):
        
        if target == 0:
            self.res.append(path)
            return
        
        if target < 0:
            return
        
        for i in range(index, len(self.candidates)):
            self.backtrack(path + [self.candidates[i]], target - self.candidates[i], i)