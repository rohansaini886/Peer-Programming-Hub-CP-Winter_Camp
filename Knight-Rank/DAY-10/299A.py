a=sorted(map(int,[*open(0)][1].split()))
print([a[0],-1][any(x%a[0] for x in a)])
