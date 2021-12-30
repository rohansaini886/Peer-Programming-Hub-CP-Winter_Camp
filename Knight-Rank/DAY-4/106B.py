n=int(input())
a=[[*map(int,input().split()),i]for i in range(n)]
a=*filter(lambda x:all(any(v>=u for u,v in zip(c[:3],x[:3])) for c in a),a),
print(min(a,key=lambda x:x[3])[4]+1)
