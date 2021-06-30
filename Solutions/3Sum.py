class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            
            lower = i + 1
            higher = len(nums) - 1
            target = 0 - nums[i]
            
            while lower < higher :
                total = nums[lower] + nums[higher]
                
                if total == target:
                    res.append([nums[i], nums[lower], nums[higher]])
                    
                    while lower < higher and nums[lower] == nums[lower+1]:
                        lower += 1
                    
                    while lower < higher and nums[higher] == nums[higher-1]:
                        higher -= 1
                    
                    lower += 1
                    higher -= 1
                
                elif total < target:
                    lower += 1
                
                elif total > target:
                    higher -= 1
        
        return res
                    