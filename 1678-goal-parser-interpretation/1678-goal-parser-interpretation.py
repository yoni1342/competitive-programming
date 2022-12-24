class Solution:
    def interpret(self, command: str) -> str:
        ptr = 0
        length =len(command)
        answer = ""
        
        while ptr<length:
            if command[ptr] == 'G':
                answer+='G'
            elif command[ptr] == '(' and command[ptr+1] == ')':
                answer+='o'
                ptr+=1
            elif command[ptr] == '(' and command[ptr+1] == 'a':
                answer+="al"
                ptr+=3
            ptr+=1
        return answer