class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        trie = set()
        
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefixes = set()
            
            for num in nums:
                prefixes.add(num & mask)
                
            temp_max = max_xor | (1 << i)
            for prefix in prefixes:
                if temp_max ^ prefix in prefixes:
                    max_xor = temp_max
                    break
        
        return max_xor