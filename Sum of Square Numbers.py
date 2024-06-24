class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        seen= set()
        for i in range(int(sqrt(c))+1):
            seen.add(i*i)
            num = c - (i*i)
            if num in seen:
                return True
        return False
