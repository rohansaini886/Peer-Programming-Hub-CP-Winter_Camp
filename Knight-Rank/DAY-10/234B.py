F=open('input.txt')
I=lambda:map(int,F.readline().split())
n,k=I();a=sorted(zip(I(),range(n)))[::-1]
print(a[k-1][0],'\n',*(y+1for x,y in a[:k]),file=open('output.txt','w'))
