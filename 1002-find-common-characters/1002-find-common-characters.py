class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hashArr = []
        for word in words:
            hashArr.append(Counter(word))
        
        common = hashArr[0]
        
        for maps in hashArr:
            common = common & maps.keys()
        
        answer = []
        
        for key in common:
            val = 101
            for maps in hashArr:
                val = min(val, maps[key])
            for i in range(val):
                answer.append(key)
        
        return answer