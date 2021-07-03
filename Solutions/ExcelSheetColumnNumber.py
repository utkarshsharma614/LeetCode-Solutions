class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        i = 1
        
        while i <= len(columnTitle):
            res += (26 ** (i-1)) * (ord(columnTitle[-i]) - 64)
            i += 1
        
        return res