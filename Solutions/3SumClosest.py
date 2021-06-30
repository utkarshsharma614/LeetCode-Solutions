class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[-1]
        
        for i in range(len(nums) - 2):
            lower = i + 1
            higher = len(nums) -1
            
            while lower < higher:
                temp = nums[i] + nums[lower] + nums[higher]
                if abs(temp - target) < abs(res - target):
                    res = temp
                
                if temp == target:
                    break
                
                elif temp < target:
                    lower += 1
                
                elif temp > target:
                    higher -= 1
        
        return res