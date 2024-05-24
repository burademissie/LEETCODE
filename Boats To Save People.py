class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res=0
        i=0
        j=len(people)-1
        while i<=j:
            space = limit - people[j]
            j-=1
            res+=1
            if i<=j and space>=people[i]:
                i+=1
        return res

        
