class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        output = float(inf)
        l = 0
        for r in range(len(blocks)):
            if blocks[r]=='W':
                countW += 1
            elif r >= k and blocks[r] == 'W':
                countW += 1
            if r >= k:
                if blocks[l] == 'W':
                    countW -= 1
                l+=1
            if r == k-1:
                output = countW
                
            output = min(output,countW)
        return output