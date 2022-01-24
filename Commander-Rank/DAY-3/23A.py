s = input()
for i in range(len(s), 0, -1):
	for j in range(len(s) - i + 1):
		if s[j: j + i] in s[j + 1:]:
			print(i)
			exit()
print(0)
