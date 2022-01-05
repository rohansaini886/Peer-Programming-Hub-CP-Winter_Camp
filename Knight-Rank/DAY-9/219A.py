k=int(input())
s=sorted(input())
x=s[::k]*k
print("".join(x) if sorted(x)==s else -1)
