class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = maxlength = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            maxlength = max(maxlength,r-l+1)
        return maxlength
        
