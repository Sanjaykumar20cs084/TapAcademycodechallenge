lst=list(map(int,input().split()))
k=int(input('Enter the target sum: '))
sumlst=[]
for i in range(len(lst)):
    for j in range(i,len(lst)):
        if sum(lst[i:j+1])==k:
            sumlst.append((lst[i:j+1]))
#print(sumlst)
print(f'Largest subarray with sum {k}:',max(sumlst,key=len))