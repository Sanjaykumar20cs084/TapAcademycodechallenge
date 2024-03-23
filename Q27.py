''' string=input('Enter the string: ')
substr=[]
for i in range(0,len(string)):
    for j in range(i,len(string)):
        substr.append(string[i:j+1])
#print(substr)
print(f'substrings:',end='')
for k in substr:
    print(k,end=' ') '''


string=input('Enter the string: ')
for i in range(0,len(string)):
    for j in range(i,len(string)):
        print(string[i:j+1],end=' ')


