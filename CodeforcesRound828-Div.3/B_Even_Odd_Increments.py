tt = int(input())
while tt:
    tt-=1
    n, q = list(map(int, input().split()))
    
    a = list(map(int, input().split()))
    oddCount=evenCount=0

    for i in a:
        if i%2==0:
            evenCount+=1
        else:
            oddCount+=1
    
    Sum = sum(a)

    for _ in range(q):
        ref, num = list(map(int, input().split()))
        
        if ref == 0:
            if num % 2 == 0:
                Sum+=(num*evenCount)
                print(Sum)
            else:
                Sum+=(num*evenCount)
                oddCount+=evenCount
                evenCount = 0
                print(Sum)
        if ref == 1: 
            if num%2 == 0:
                Sum+=(num*oddCount)
                print(Sum)
            else:
                Sum+=(num*oddCount)
                evenCount+=oddCount
                oddCount=0
                print(Sum)
