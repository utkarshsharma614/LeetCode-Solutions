class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set()
        
        for num in nums:
            numSet.add(num)
            
        output = 0
        for num in numSet:
            count = 1
            if num-1 not in numSet:
                while num+1 in numSet:
                    count += 1
                    num += 1
                
                output = max(output, count)
        
        return output
        