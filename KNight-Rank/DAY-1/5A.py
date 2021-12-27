k ,m= 0,0
while True:
	try:
		line = str(input())
	except:
		break
	if line[0] == '+':
		m +=1
	elif line[0] == '-':
		m -= 1
	else:
		k += m*len(line[line.index(':')+1::])
print(k)
