string=input('Enter the string: ')
dic={}
for i in string:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for key,value in dic.items():
    print(f'{key}-{value},',end=' ')