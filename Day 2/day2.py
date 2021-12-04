x = open('input.txt', 'r')
i_a = []
for line in x.readlines():
    i_a.append(line.replace('\n', ''))

# print(i_a[1][5])

# forward 8
horizontal = 0
vertical = 0
aim = 0

for item in i_a:
    if item.startswith('f'):
        horizontal += int(item[8])
        vertical += int(item[8]) * aim
    elif item.startswith('d'):
        aim += int(item[5])
    else:   
        aim -= int(item[3])

print(horizontal*vertical)

    