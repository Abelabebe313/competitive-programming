from collections import *
class Solution:
    def findOrder(self,alien, N, K):
    # code here
        graph = defaultdict(list)
        Indg = defaultdict(int)
        for i in range(N-1):
            word1 = alien[i]
            word2 = alien[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    Indg[word2[j]] += 1
                    break
        qu = deque()
        for i in range(k):
            if chr(97 + i) not in Indg:
                qu.append(chr(97 + i))
        ans = []
        while qu:
            node = qu.popleft()
            ans.append(node)
            for nbr in graph[node]:
                 Indg[nbr] -= 1
                 if Indg[nbr] == 0:
                     qu.append(nbr)
        
        return ''.join(ans)
        