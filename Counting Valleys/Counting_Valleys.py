def countingValleys(steps, path):
    # Write your code here
    arr = list(path)
    valleys = 0
    up =[]
    down = []
    
    for i in arr:
        if(i=='U'):
            up.append(i)
        elif(i=="D"):
            if(len(up)==len(down)):
                valleys+=1
            down.append(i)
    
    return valleys