lst=list(map(int,input().split()))
k=int(input("enter the target sum: "))
print(f'Subarrays with Sum {k}:')
for i in range(0,len(lst)):
    for j in range(i,len(lst)):
        if sum(lst[i:j+1])==k:
            print(lst[i:j+1])