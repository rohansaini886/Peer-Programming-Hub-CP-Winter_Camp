I=input
s=I()
C={}
for x in set(s):C[x]=s.count(x)
k=int(I())
t=sorted(set(s),key=lambda x:C[x])
while t and C[t[0]]<=k:k-=C[t[0]];s=s.replace(t[0],'');t=t[1:]
print(len(set(s)))
print(s)
