input()
L = sorted(int(x)*int(x) for x in input().split())
print(3.1415926536 * (sum(L[::-2])-sum(L[-2::-2])))
