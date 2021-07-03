class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = len(nums)-1
        stack = []
        mx = float('-inf')
        
        for i, n in enumerate(nums):
            while stack and stack[-1][1] > n:
                candidate = stack.pop()
                l = min(l, candidate[0])
                mx = max(mx, candidate[1])
            stack.append((i, n))
        
        if l == len(nums)-1:
            return 0
        r = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < mx:
                r = i
                break
        return r - l + 1
        
                