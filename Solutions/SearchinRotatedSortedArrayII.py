class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return True
            
            if nums[l] == nums[mid] and nums[r] == nums[mid]:
                l, r = l + 1, r - 1
            
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return False