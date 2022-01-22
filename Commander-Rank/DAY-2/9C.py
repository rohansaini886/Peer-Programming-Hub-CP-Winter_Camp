n=input()
r=0
for i in range(1, 2**9+1):
    r+=(int(bin(i)[2:]) <= int(n))
print(r)
