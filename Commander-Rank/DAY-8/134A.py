n=int(input())
a=list(map(int,input().split()))
p=[]
s=sum(a)
for i in range(n):
	if (s-a[i])==a[i]*(n-1):
		p.append(i+1)
print(len(p))
print(*p)
