class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        Dict = defaultdict(int)
        
        def GCD(a,b):
            if b == 0:
                return a
            return GCD(b,a % b)
        
        for i in range(len(deck)):
            Dict[deck[i]] += 1
        
        mini = float('inf')
        card_count = list(Dict.values())
        
        if len(card_count) == 1:
            mini = card_count[0]
        else:
            for i in range(len(card_count)-1):
                mini = min(mini, GCD(card_count[i],card_count[i+1]))

        
        if mini > 1:
            return True
        return False
        