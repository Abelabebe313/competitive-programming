class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        result = right
        while left <= right:
            k = (left + right)//2
            # print(k)
            total = 0
            count = 0
            for weight in weights:
         
                if total + weight > k:
                    count += 1
                    total = 0
                total += weight
       
            if total:
                count += 1
            if count <= days:
                result =min(result,k)
                right = k - 1
            else:
                left = k + 1
        return result
                    
                
                