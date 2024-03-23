arr=[]
n=int(input("enter the size of array"))
for i in range(n):
    arr.append(int(input("enter number")))
k=int(input("enter the difference :" ))
op=[]
for j in range(len(arr)):
    for l in range(j+1,len(arr)):
        if arr[j]-arr[l]==k or arr[l]-arr[j]==k:
            op.append((arr[j],arr[l]))
#print(op)
for m in op:
    print(m,end=" ")


