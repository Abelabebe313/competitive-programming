class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons = persons
        self.times = times
        
        self.leading_nums = []
        self.counter = defaultdict(int)
        self.leading_nums.append(persons[0])
        self.counter[persons[0]] += 1
        
        for i in range(1, len(persons)):
            self.counter[persons[i]] += 1
            if self.counter[persons[i]] >= self.counter[self.leading_nums[-1]]:
                self.leading_nums.append(persons[i])
            else:
                self.leading_nums.append(self.leading_nums[-1])
                             
    def q(self, t: int) -> int:
        idx = bisect_right(self.times,t)-1
        return self.leading_nums[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)