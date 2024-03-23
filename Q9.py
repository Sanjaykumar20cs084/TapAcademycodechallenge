''' arr=list(map(int,input().split()))
max=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max=arr[i]
print(max) '''

arr=list(map(int,input().split()))
lar=arr[0]
i=1
while i<len(arr):
    if arr[i]>lar:
        lar=arr[i]
    i+=1
print(lar)
#print(max(arr))