class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strg=str(x)
        reverse=strg[::-1]
        if strg==reverse :
            return bool(1)
        else :
            return bool(0)
            