from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        
        for i in range(numRows):
            temp = []
            
            for j in range(i+1):
                temp.append(factorial(i)//(factorial(i-j) * factorial(j)))
            
            output.append(temp)
        
        return output