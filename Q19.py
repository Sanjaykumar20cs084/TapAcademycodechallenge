'''string=input("Enter the string to reverse")
#print(string[::-1])
string1="" '''

'''for i in range(len(string),0,-1):
       string1+=string[i-1]
print(string1) '''

''' i=len(string)
while i>0:
    string1+=string[i-1]
    i-=1
print(string1) '''

#using recursion:
string1=input()
def reverse(string1):
  string2=''
  if len(string1)==1:
        return string1
  else:
        return string1[-1]+reverse(string1[:-1])
print(reverse(string1))
