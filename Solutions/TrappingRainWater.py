class Solution:
    def trap(self, height: List[int]) -> int:
        def trap(height):
            l, r = 0, len(height) - 1
            left_max, right_max = 0, 0
            res = 0
            
            while l < r:
                left_max = max(left_max, height[l])
                right_max = max(right_max, height[r])
                
                if left_max <= right_max:
                    res += (left_max - height[l])
                    l += 1
                
                else:
                    res += (right_max - height[r])
                    r -= 1
            return res
        
        return trap(height)