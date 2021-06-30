class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = ["[", "{", "("] 
        close = ["]", "}", ")"]
        stack1 = []
        for i in s:
            if i in open :
                stack1.append(i)
            elif i in close :
                pos = close.index(i)
                if ((len(stack1) > 0) and (open[pos] == stack1[len(stack1)-1]) ):
                        stack1.pop()
                else :
                    return bool(0)
        
        if len(stack1) == 0:
            return bool(1)
        else :
            return bool(0)
                
        