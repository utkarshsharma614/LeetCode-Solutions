class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=0
        x=s.strip()
        for i in range (len(x)):
                if x[i]==" " :
                    l=0
                else :
                    l=l+1
        return l