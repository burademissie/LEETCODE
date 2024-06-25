class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        spaces = set(spaces)
        for i,c in enumerate(s):
            if i in spaces:
                ans.append(' ')
            ans.append(c)
        return "".join(ans)
        
