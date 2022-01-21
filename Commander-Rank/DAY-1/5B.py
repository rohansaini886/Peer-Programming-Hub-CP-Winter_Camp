import sys

lines = []
maxlen = 0
for line in sys.stdin:
	lines.append(line.rstrip())
	maxlen = max(maxlen, len(lines[-1]))

print('*' * (maxlen + 2))

left = True
for line in lines:
	s = maxlen - len(line)
	a = s // 2
	b = s - a
	if a != b:
		if not left:
			a, b = b, a
		left = not left
	print('*' + (' ' * a) + line + (' ' * b) + '*')

print('*' * (maxlen + 2))
