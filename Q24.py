string=input('Enter the string:')
vowels=['A','E','I','O','U','a','e','i','o','u']
string1=''
for i in string:
    if i in vowels:
       string1+='#'+i
    else:
        string1+=i
print(string1)