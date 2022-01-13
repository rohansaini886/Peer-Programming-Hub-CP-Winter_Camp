F=open('input.txt','r')
W=open('output.txt','w')
I=lambda:[*map(int,F.readline().split())]
n,k=I()
k-=1
a=I()
while a[k]<1:k=(k+1)%n
W.write(str(k+1))
W.close()
