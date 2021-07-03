class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res