string=input('Enter the string: ')
charc=input('Enter the character: ')
lastindex=0
for i in range(0,len(string)):
    if string[i]==charc:
        lastindex=i
print(f'Lastindex:',lastindex)
