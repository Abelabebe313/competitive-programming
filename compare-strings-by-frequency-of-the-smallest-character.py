class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        queries_list = []
        words_list = []
        for qr in queries:
            queries_list.append(qr.count(min(qr)))
        for wr in words:
            words_list.append(wr.count(min(wr)))

        words_list.sort()
        
        ans = []
        for target in queries_list: 
            right = bisect_right(words_list,target)
            ans.append(len(words_list)-right)
        return ans