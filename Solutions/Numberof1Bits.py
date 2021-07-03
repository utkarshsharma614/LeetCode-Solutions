class Solution:
    def hammingWeight(self, n: int) -> int:
        l = list("{:032b}".format(n))
        
        l[:] = (value for value in l if value != '0')
        
        return len(l)
        