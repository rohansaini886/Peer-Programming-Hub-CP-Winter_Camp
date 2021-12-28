F=open('input.txt','r')
W=open('output.txt','w')
I=lambda:[*map(int,F.readline().split())]
x=I()[0]
for _ in[0]*3:
  u,v=I()
  if x==u:x=v
  elif x==v:x=u
W.write(str(x))
W.close()
