class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = {}
        visited = set()
        
        for i in range(len(indices)):
            start = indices[i]
            source = sources[i]
            end = start + len(source)
            if s[start : end] == source:
                res[start] = targets[i]
                for j in range(start, end):
                    visited.add(j)
        
        output = ""
        
        for i in range(len(s)):
            if i in res:
                output += res[i]
            elif i not in visited:
                output += s[i]
        
        return output