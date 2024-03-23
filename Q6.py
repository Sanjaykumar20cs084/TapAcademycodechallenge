''' n1=int(input())
n2=int(input())
common_fact=[]
for i in range(1,n1+1):
    if n1%i==0 and n2%i==0:
        common_fact.append(i)
print(f"H.C.F of the two numbers {n1} and {n2} is",max(common_fact)) '''

n1=int(input())
n2=int(input())
hcf=1
i=1
while i<=n1+1:
    if n1%i==0 and n2%i==0:
        hcf=i
    i+=1
print(hcf)