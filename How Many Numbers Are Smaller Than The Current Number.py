class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        less = 0
        res = [0]*len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i]>nums[j]:
                    less+=1
            res[i]=less
            less=0
        return res
            
        
