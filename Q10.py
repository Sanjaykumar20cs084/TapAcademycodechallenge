arr=list(map(int,input().split()))
ele=int(input())
Occur=0
for i in range(len(arr)):
    if arr[i]==ele:
        Occur+=1
print(Occur)
#print(f"the element {ele} occurs {Occur} times in {arr} this array")
occurs=arr.count(2)
print(occurs)
#print(f"the element {ele} occurs {occurs} times in {arr} this array")