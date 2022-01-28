I=lambda:map(int,input().split())
n,m=I()
N=list(I())
p=set()
for i in range(m):
	x,y=I();x-=1;y-=1
	p.add((x,y)if x<y else(y,x))
r=1e9
for i in range(n):
	for j in range(i):
		for k in range(j):
			if(j,i)in p and(k,i)in p and(k,j)in p:
				r = min(r,N[i]+N[j]+N[k])
print(-1 if r>1e8 else r)
