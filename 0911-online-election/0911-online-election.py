class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.ref = []
        
        Hash = defaultdict(lambda:[0,0])
        
        for i in range(len(times)):
            Hash[persons[i]][0] += 1
            Hash[persons[i]][1] = times[i]
            
            person = max(Hash, key=Hash.get)
            self.ref.append((times[i], person)) 

    def q(self, t: int) -> int:
        return self.ref[bisect.bisect_right(self.times, t) - 1][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)