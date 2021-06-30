class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=2**31-1 or x<=-(2**31) : return 0
        else :
            strg=str(x)
            if x>=0:
                reverse=strg[::-1]
            else:
                temp=strg[1:]
                temp1=temp[::-1]
                reverse="-"+temp1
            if int(reverse) >=2**31-1 or int(reverse) <=-(2**31) : return 0
            else : return int(reverse)