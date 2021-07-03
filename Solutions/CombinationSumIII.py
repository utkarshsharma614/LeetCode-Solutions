class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def backtrack(num, stack, target):
            
            if len(stack) == k and target == 0:
                res.append(stack)
                return
            
            for i in range(num + 1, 10):
                if i <= target:
                    backtrack(i, stack + [i], target - i)
        
        backtrack(0, [], n)
        
        
        return res