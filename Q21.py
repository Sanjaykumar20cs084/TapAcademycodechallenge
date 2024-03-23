string=input("Enter the string:")
vowels=['A','E','I','O','U','a','e','i','o','u']
strvowels=[]
count=0
for i in string:
    if i in vowels:
        count+=1
print(f'Number of Vowels:',count)
''' strvowels.append(i)
print(f'the vowels in the string {string} are',end=' ')
for j in strvowels:
    print(j,end=' ')
print(f'and the count is {count}') '''