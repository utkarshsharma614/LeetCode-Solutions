class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictC = {}
        dictB = {}
        
        for i in range(len(s)):
            if s[i] in dictC:
                if dictC[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dictB:
                    return False
                else:
                    dictC[s[i]] = t[i]
                    dictB[t[i]] = True
        
        return True