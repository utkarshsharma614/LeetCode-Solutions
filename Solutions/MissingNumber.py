class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        sum_= int((n/2)*(n-1))
        
        return sum_ - sum(nums)