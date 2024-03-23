num=int(input())
ans=num
rev=0
while num!=0:
    rev=rev*10+num%10
    num//=10
#print(rev)
if ans==rev:
    print("palindrome")
else:
    print("not a palindrome")