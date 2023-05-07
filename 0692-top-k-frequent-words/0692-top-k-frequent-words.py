class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countWord = defaultdict(int)
        for word in words:
            countWord[word] += 1
        
        heap = []
        
        for key,val in countWord.items():
            heappush(heap,(-val,key))
        
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
            
        return ans
        
        