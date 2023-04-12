class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        dislike_dict = defaultdict(list)
        
        for i in range(len(dislikes)):
            a,b = dislikes[i]
            dislike_dict[a].append(b)
            dislike_dict[b].append(a)
        colors = [0] * (n+1)
        
        def flip_Color(color):
            if color == 1:
                return -1
            return 1
        
        def DFS(node,color):
            if colors[node] != 0:
                return colors[node]==color
            
            colors[node] = color
            next_color = flip_Color(color)
            
            result_holder = []
            for child in dislike_dict[node]:
                result_holder.append(DFS(child,next_color))
            return all(result_holder)
        
        ans = []
        for i in range(1,n+1):
            ans.append(colors[i] != 0 or DFS(i,1))
        return all(ans)