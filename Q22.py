string=input('Enter the string:')
special_char=['!','~','`','@','#','$','%','^','&',',',';',':',' ']
string1=" "
for i in string:
    if i not in special_char:
        string1+=i
print(string1)