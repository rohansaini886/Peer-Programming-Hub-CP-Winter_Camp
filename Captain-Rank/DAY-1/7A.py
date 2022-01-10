t = [input().count('B') for i in range(8)]
print(t.count(8) + min(t)%8)
