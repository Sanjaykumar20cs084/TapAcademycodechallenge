string=input("Enter the String:")
#print(string.swapcase())
string1=''
for i in string:
    ch=ord(i)
    if ch>=65 and ch<=90:
        string1+=chr(ch+32)
    elif ch>=97 and ch<=122:
        string1+=chr(ch-32)
print(string1)
