class Solution:
    def fractionToDecimal(self, num: int, denom: int) -> str:
        n, remainder = divmod(abs(num), abs(denom))
        if num * denom < 0:
            sign = '-'
        else:
            sign = ''
        
        fraction = [sign + str(n)]
        if remainder == 0:
            return ''.join(fraction)
        fraction.append('.')
        dict = {}
        
        while remainder != 0:
            if remainder in dict:
                fraction.insert(dict[remainder], '(')
                fraction.append(')')
                break
            
            dict[remainder] = len(fraction)
            n, remainder = divmod(remainder * 10, abs(denom))
            fraction.append(str(n))
        
        return ''.join(fraction)