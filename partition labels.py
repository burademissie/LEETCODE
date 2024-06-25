class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lindex = {}
        for index , char in enumerate(s):
            lindex[char]=index
        size , end = 0 , 0
        res = []
        for i , j in enumerate(s):
            size+=1
            end = max(end,lindex[j])
            if i==end:
                res.append(size)
                size = 0
        return res

