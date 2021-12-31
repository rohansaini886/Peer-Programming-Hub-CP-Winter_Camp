I=input
k=int(I())
l=int(I())
r=1
while k**r<l:r+=1
print(['NO','YES\n'+str(r-1)][k**r==l])
