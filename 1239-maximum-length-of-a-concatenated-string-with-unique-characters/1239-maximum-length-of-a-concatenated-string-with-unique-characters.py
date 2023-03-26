class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        
        def backtrack(idx, path):
            nonlocal ans
            
            # Check if path has unique characters
            if len(set(''.join(path))) == len(''.join(path)):
                ans = max(ans, len(''.join(path)))
            
            for i in range(idx, len(arr)):
                # Check if current string has unique characters
                if len(set(arr[i])) == len(arr[i]):
                    path.append(arr[i])
                    backtrack(i + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return ans
