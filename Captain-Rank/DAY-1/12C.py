S=sorted
R=input
I=lambda:map(int,R().split())
n,m=I()
C=S(I())
d={}
for _ in'0'*m:t=R();d[t]=d.get(t,0)+1
d=S(d.values())[::-1]
for c in C,C[::-1]:print(sum(d[i]*c[i]for i in range(len(d))),end=' ')
