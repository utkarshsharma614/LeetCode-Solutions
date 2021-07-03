class Solution:
    def reverseBits(self, n: int) -> int:
        l = list("{:032b}".format(n))
        
        l = l[::-1]
        
        return int(''.join(l), 2)