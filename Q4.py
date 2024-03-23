''' n1=int(input())
n2=int(input())
for i in range(1,n1+1):
    if n1%i==0:
        if n2%i==0:
            print(i,end=' ') '''
n1=int(input())
n2=int(input())
def prime(n1,n2):
    for i in range(1,n1+1):
        if n1%i==0 and n2%i==0:
            print(i,end=' ')
prime(n1,n2)