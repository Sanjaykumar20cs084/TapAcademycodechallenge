n1=int(input())
n2=int(input())
y=int(input())
common_multip=[]
i=1
while len(common_multip)<y:
    if i%n1==0 and i%n2==0:
        common_multip.append(i)
    i+=1
for i in common_multip:
    print(i,end=' ')
#common factors:
''' n1=int(input())
n2=int(input())
y=int(input())
common_fact=[]
i=1
while len(common_fact)<y:
    if n1%i==0 and n2%i==0:
        common_fact.append(i)
    i+=1
for i in common_fact:
    print(i,end=' ') '''