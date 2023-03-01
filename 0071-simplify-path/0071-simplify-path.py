class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = ['']
        path.pop(0)
        if path[-1] == '':
            path.pop()

            
        for index, val in enumerate(path):
            if val == '..' and len(stack)!=1:
                stack.pop()
            elif val != '.' and val!='..' and val!='':
                stack.append(val)
    
        return '/' if len(stack)==1 else '/'.join(stack)