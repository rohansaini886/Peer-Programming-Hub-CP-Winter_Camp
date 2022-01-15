I=input
S=sorted
n=int(I())
s=I()
print(['YES','NO'][abs(sum([(i<j)-(j<i)for i,j in zip(S(s[:n]),S(s[n:]))]))<n])
