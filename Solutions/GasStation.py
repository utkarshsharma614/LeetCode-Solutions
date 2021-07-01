class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        tank = 0
        shortage = 0
        for index in range(len(gas)):
            tank += gas[index]
            if tank >= cost[index]:
                tank -= cost[index]
            else:
                shortage += cost[index] - tank
                tank = 0
                start = index + 1
        
        if start == len(gas) or tank < shortage:
            return -1
        
        return start