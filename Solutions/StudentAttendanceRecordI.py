class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == 'A':
                count += 1
            if count >= 2:
                return False
        
        if 'LLL' in s:
            return False
        
        return True