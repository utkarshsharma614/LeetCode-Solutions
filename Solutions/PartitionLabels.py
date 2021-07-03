class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {char : index for index, char in enumerate(s)}
        l = 0
        r = 0
        res = []
        
        for index, char in enumerate(s):
            r = max(r, d[char])
            if index == r:
                res.append(r - l + 1)
                l = r + 1
        
        return res