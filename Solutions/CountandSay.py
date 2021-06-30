class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        if n==2:
            return "11"
        s="11"
        for i in range (3,n+1):
                    s=s+"$"
                    l=len(s)
                    count=1
                    tmp=""
                    for j in range (1,l):
                            if (s[j]!=s[j-1]) :
                                    tmp=tmp+str(count)
                                    tmp=tmp+s[j-1]
                                    count=1
                            else :
                                    count=count+1
                    s=tmp
        return s