class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        vowels = set('aeiouAEIOU')

        for x in range(len(words)):
            if words[x][0] in vowels:
                words[x] += "ma"
            else:
                words[x] = words[x][1:] + words[x][0]
                words[x] += "ma"
        
            words[x] += (x+1) * "a"
    
        return " ".join(words)