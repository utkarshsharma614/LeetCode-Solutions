class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for x in range(len(s)-9):
            if s[x:x+10] not in d:
                d[s[x:x+10]]=0
            d[s[x:x+10]] += 1
        
        return [key for key,vals in d.items() if vals>1]
                