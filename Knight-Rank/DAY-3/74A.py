a=[]
for s in [*open(0)][1:]:
  s=s.split()
  a+=[[s[0],*map(int,s[1:])]]
print(max(a,key=lambda x:x[1]*100-x[2]*50+sum(x[3:]))[0])
