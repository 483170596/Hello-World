t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    list_n = list(map(int,input().split()))
    count_1 = 0
    count_2 = 0
    left = n+1
    right = -1
    list_m = [0]*m
    for j in list_n:
        if j == -1:
            count_1+=1
        elif j==-2:
            count_2+=1
        else:
            if left > j:
                left = j
            if right < j:
                right = j
            list_m[j-1] = 1
    if count_1 + count_2 >= m:
        print(m)
    else:
        count_0 = (right - left + 1)-sum(list_m[left-1:right-1])
        left = left -1
        right = m -right
        if count_0 + left + right <= count_1+count_2:
            print(m)
        else:
            print(count_1+count_2+sum(list_m))
    
        