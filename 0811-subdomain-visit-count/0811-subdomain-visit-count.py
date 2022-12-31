class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        CountHash = defaultdict(int)
        
        for cpdomain in cpdomains:
            count = int(cpdomain.split()[0])
            domain = cpdomain.split()[1]
            
            CountHash[domain] += count
            
            for i in range(len(domain)):
                if domain[i] == '.':
                    CountHash[domain[i+1:len(domain)]] += count
        
        answer = [f"{CountHash[i]} {i}" for i in CountHash]
        return answer