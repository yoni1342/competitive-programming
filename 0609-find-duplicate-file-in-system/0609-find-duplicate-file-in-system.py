class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        
        for path in paths:
            destructure = path.split()
            directory = destructure[0]
            
            for fileptr in range(1,len(destructure)):
                file = destructure[fileptr].split("(")[0]
                content = destructure[fileptr].split('(')[1]
                content = content[0:len(content)-1]
                count[content].append(directory+'/'+file)
        
        answer = [x for x in count.values() if len(x) > 1]
        
        return answer