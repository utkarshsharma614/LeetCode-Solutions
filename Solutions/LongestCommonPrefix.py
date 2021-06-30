class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs : return ""
        n=len(strs)
        strs.sort()
        str1 = strs[0]
        str2 = strs[n-1]
        n1 = len(str1)
        n2 = len(str2)
        result = ""
        i=0
        j=0
        while (i <= n1-1 and j <= n2-1) : 
               if (str1[i] != str2[j]):
                     break
               result = result + str1[i]
               i = i + 1 
               j = j + 1
            
        return (result)