lst=list(map(int,input().split()))
dic={}
for i in lst:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for key,value in dic.items():
    print(f'{key}-{value}')