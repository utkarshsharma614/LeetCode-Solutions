class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        
        for index in range(1, len(s) + 1):
            for word in wordDict:
                if dp[index - len(word)] and s[:index].endswith(word):
                    dp[index] = True
        
        return dp[-1]