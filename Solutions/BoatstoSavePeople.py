class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        A,B,res = 0, len(people) - 1, 0
        
        while A <= B:
            if people[A]+people[B] <=limit :
                    A+=1
                    
            B-=1
            res+=1
            
        return res