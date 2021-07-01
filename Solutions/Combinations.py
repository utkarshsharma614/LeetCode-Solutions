class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(num, stack):
            if len(stack) == k:
                res.append(stack)
                return
            
            for i in range(num+1, n+1):
                backtrack(i, stack + [i])
        
        
        backtrack(0, [])
        
        return res