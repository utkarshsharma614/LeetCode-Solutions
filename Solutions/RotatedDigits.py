class Solution:
    def rotatedDigits(self, n: int) -> int:
        def good(i):
            return ('2' in str(i) or '5' in str(i) or '6' in str(i) or '9' in str(i)) and ('3' not in str(i) and '4' not in str(i) and '7' not in str(i))
        
        count = 0
        for i in range(1, n+1):
            if good(i):
                count += 1
        
        return count