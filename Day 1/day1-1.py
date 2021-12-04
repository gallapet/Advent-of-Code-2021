x = open('input.txt', 'r')
i_a = []
for line in x.readlines():
    i_a.append(line.replace('\n', ''))

increases = 0

for i in range(1, len(i_a)-2):
    if int(i_a[i+2]) + int(i_a[i+1]) + int(i_a[i]) > int(i_a[i+1]) + int(i_a[i]) + int(i_a[i-1]):
        increases += 1

print(increases)