class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = 0
        for char in s:
            diff ^= ord(char)
        for char in t:
            diff ^= ord(char)
        
        return chr(diff) 