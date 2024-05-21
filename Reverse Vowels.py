class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        
        slist=list(s)
        i=0
        j=len(slist) - 1
        while(i<j):
            if slist[j] not in vowel:
                j-=1
                continue
            if slist[i] not in vowel:
                i+=1
                continue
            
            slist[i] , slist[j] = slist[j] , slist[i]
            i+=1
            j-=1
                
            
        return "".join(slist)
        
