class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        score=0
        l,r = 0, len(tokens)-1
        while l<=r and (score or P>=tokens[l]):
            if P>= tokens[l]:
                score+=1
                P-=tokens[l]
                l+=1
                
            elif l!=r:
                score-=1
                P+=tokens[r]
                r-=1
                
            else:
                break
        
        return score