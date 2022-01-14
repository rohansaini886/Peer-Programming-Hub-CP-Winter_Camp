v=[]
r=0
k=1
for _ in range(int(input())):
    a,b=map(int,input().split())
    if b==0:v+=[a]
    else: r,k=r+a,k+b-1
print(r+sum((sorted(v)[::-1])[:min(len(v),k)]))
