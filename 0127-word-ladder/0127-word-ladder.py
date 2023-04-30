class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        que = deque([(beginWord, 1)])
        
        visited = set([beginWord])
        
        while que:
            word, level = que.popleft()
            
            for i in range(len(word)):
                for letter in 'acbdefghijklmnopqrstuvwxyz':
                    if letter == word[i]:
                        continue
                    
                    newWord = word[:i] + letter + word[i+1:]
                
                    if newWord in wordList and newWord not in visited:
                        if newWord == endWord:
                            return level+1
                    
                        que.append((newWord, level+1))
                    visited.add(newWord)
        return 0