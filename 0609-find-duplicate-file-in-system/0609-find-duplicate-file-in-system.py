class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        
#       splite all Path with space and the first one is the directory path
#       after spliting we search the content name and we store the content name as key and the file path 
#       as value with list in dictonary 
        for path in paths:
            destructure = path.split()
            directory = destructure[0]
            
            for fileptr in range(1,len(destructure)):
                file = destructure[fileptr].split("(")[0]
                content = destructure[fileptr].split('(')[1]
                content = content[0:len(content)-1]
                count[content].append(directory+'/'+file)
#       after we sore in dict then we'll  create answer list that contain only elements that has two or more values or file path 
        answer = [x for x in count.values() if len(x) > 1]
        
        return answer
