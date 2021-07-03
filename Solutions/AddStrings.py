class Solution:
    def addStrings(self, nums1: str, nums2: str) -> str:
        res = []
        i = len(nums1) -1 
        j = len(nums2) - 1
        carry = 0
        
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += ord(nums1[i]) - 48
                i -= 1
            if j >= 0:
                _sum += ord(nums2[j]) - 48
                j -= 1
            res.append(_sum%10)
            carry = _sum // 10
        
        if carry != 0:
            res.append(carry)
            
        res = res[::-1]
        
        return ''.join(str(e) for e in res)