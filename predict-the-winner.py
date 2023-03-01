class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def prediction(start,end,PlayerTurn):
            if start == end:
                if PlayerTurn:
                    return [nums[start],0]
                else:
                    return [0,nums[start]]
                
            chance1 = prediction(start+1,end, not PlayerTurn)
            chance2 = prediction(start,end-1, not PlayerTurn)
            
            if PlayerTurn:
                if chance1[0] + nums[start] > chance2[0] + nums[end]:
                    chance1[0] += nums[start]
                    return chance1
                else:
                    chance2[0] += nums[end]
                    return chance2
            else:
                if chance1[1] + nums[start] > chance2[1] + nums[end]:
                    chance1[1] += nums[start]
                    return chance1
                else:
                    chance2[1] += nums[end]
                    return chance2
        
        player1, player2 = prediction(0, len(nums)-1, True)
        print(player1,player2)
        if player1 >= player2:
            return True
        else:
            return False