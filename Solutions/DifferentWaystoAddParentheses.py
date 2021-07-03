class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        res = []
        for i in range(len(exp)):
            char = exp[i]
            if char == "+" or char == "-" or char == "*":
                a = exp[0 : i]
                b = exp[i + 1 : ]
                al = self.diffWaysToCompute(a)
                bl = self.diffWaysToCompute(b)
                for x in al:
                    for y in bl:
                        if char == "+":
                            res.append(x + y)
                        elif char == "-":
                            res.append(x - y)
                        elif char == "*":
                            res.append(x * y)
        if not len(res):
            res.append(int(exp))
        return res