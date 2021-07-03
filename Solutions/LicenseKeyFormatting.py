class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        result = ''
        count = 0
        for char in s:
            if count == k:
                result += '-'
                count = 0
            
            result += char
            count += 1
        
        return result[::-1]