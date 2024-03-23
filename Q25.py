string=input('Enter the string: ')
charc=input('Enter the character: ')
for i in range(0,len(string)):
    if string[i]==charc:
        #print(f'the character {charc} is present in the string {string} at the index {i}')
        print(i)
        break