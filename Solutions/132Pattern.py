class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins_list = []
        stack = []
        
        mins_list.append(nums[0])
        for i in range(1, len(nums)):
            mins_list.append(min(nums[:i]))
            
        for j in range (len(nums)-1, -1, -1):
            if nums[j] > mins_list[j]:
                while stack and stack[-1] <= mins_list[j]:
                    stack.pop()
                
                if stack and stack[-1] < nums[j]:
                    return True
                
                stack.append(nums[j])
        
        return False