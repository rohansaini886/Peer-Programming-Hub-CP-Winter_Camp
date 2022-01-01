r=range;N=int(input())
for i in[*r(N),*r(N,-1,-1)]:print(*' '*(N-i),*r(i+1),*r(i-1,-1,-1))
