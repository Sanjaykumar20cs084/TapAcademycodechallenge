lst=list(map(int,input().split()))
for i in range(0,len(lst)):
    for j in range(i,len(lst)):
        print(lst[i:j+1])
