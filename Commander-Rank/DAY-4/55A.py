n = int(input())
print('YNEOS'[n & (n - 1) > 0 :: 2])
