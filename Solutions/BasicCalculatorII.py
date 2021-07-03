class Solution:
    def calculate(self, s: str) -> int:
        stack, currNum, op = [], 0, "+"
        operators = {"+", "-", "*", "/"}
        nums = set(str(i) for i in range(10))
        
        for index in range(len(s)):
            char = s[index]
            
            if char in nums:
                currNum = currNum * 10 + int(char)
            
            if char in operators or index == len(s)-1:
                if op == "+":
                    stack.append(currNum)
                
                elif op == "-":
                    stack.append(-currNum)
                
                elif op == "*":
                    stack[-1] *= currNum
                
                elif op == "/":
                    stack[-1] = int(stack[-1]/currNum)
                
                op = char
                currNum = 0
                
        
        return sum(stack)
        