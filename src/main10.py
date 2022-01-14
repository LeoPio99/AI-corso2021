l = []
with open('input.txt', 'r')
as f:
for line in f:
line = line.strip()
if len(line) > 0:
l.append(map(int, line.split(',')))
print(l)