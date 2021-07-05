class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.dp = [0] * len(days)
        self.days = days
        self.costs = costs
        return self.minCost(0)
    
    def minCost(self, index):
        
        if index == len(self.days):
            return 0
        
        if self.dp[index] != 0:
            return self.dp[index]
        
        self.dp[index] = min(self.costs[0] + self.minCost(self.nday(index, 1)), self.costs[1] + self.minCost(self.nday(index, 7)), self.costs[2] + self.minCost(self.nday(index, 30)))
        
        return self.dp[index]
    
    def nday(self, index, duration):
        temp = index
        nextDay = self.days[index] + duration - 1
        
        while temp < len(self.days) and self.days[temp] <= nextDay:
            temp += 1
        
        return temp