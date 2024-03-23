array=list(map(int,input().split()))
pair=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        pair.append((array[i],array[j]))
#print(pair)
for i in pair:
    print(i,end=" ")

