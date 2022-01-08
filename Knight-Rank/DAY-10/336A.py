x,y=map(int,input().split())
a=abs(x)+abs(y)
v=[-a,a][y>0]
print(*((-a,0,0,v)if x<0 else(0,v,a,0)))
