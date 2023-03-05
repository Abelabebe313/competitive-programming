class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.Data = {value:0}
    def consec(self, num: int) -> bool:
        if num == self.val:
            self.Data[self.val] += 1
        else:
            self.Data[self.val] = 0
            
        if self.Data[self.val] >= self.k:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)