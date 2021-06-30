class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        sort_candidates = sorted(candidates)
        self.sort_candidates = sort_candidates
        # self.candidates = candidates
        self.backtrack([], target, 0)
        # final = self.res
        # final.sort()
        # return list(final for final,_ in itertools.groupby(final))
        # return list(self.res)
        return self.res
    
    def backtrack(self, path, target, index):
        
        if target == 0:
            self.res.append(path)
            return
        
        if target < 0:
            return
        
        # sort_candidates = sorted(self.candidates)
        
        for i in range(index, len(self.sort_candidates)):
            if i == index or self.sort_candidates[i] != self.sort_candidates[i-1]:                  self.backtrack(path + [self.sort_candidates[i]], target - self.sort_candidates[i], i + 1)