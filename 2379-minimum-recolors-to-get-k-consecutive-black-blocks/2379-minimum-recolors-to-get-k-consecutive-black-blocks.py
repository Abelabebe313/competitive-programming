class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        output= float('inf')
        r = k
        for i in range(len(blocks)-k+1):
            for j in range(i,r):
                if blocks[j] == 'W':
                    count += 1
            r += 1
            output = min(output, count)
            count = 0
        return output