class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        N1 = len(word1)
        N2 = len(word2)
        
        i = 0
        j = 0

        while i < N1 and j < N2:

            if word1[i] > word2[j]:
                merge.append(word1[i])
                i += 1
            elif word1[i] < word2[j]:
                merge.append(word2[j])
                j += 1
            else:
                if word1[i+1:] >= word2[j+1:]:
                    merge.append(word1[i])
                    i += 1
                else:
                    merge.append(word2[j])
                    j += 1

        return ''.join(merge) + word1[i:] + word2[j:]
        
