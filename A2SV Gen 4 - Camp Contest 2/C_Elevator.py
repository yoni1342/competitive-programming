t = int(input())

for i in range(t):
    wt, et, ef = map(int, input().split())

    elevator_time = (4-ef) * et
    
    walk_time = (4-ef) * wt
    
    min_time_after = min(elevator_time, walk_time)

    min_time_befor = min(et*ef*2, wt*ef)

    print(min_time_after + min_time_befor)      