lst=list(map(int,input().split()))
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
''' print(dic)
dic.pop(1)
print(max(dic,key=dic.get)) '''
large=max(dic.values())
for key,value in dic.items():
    if value==large:
        largest_key=key       
print(largest_key)