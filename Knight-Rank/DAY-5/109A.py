n=int(input())
a,b=n//7,n%7
c,d=b//4,b%4
print(-1if a<d else'4'*(c+2*d)+'7'*(a-d))
