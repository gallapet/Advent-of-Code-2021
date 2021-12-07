x = open('test.txt', 'r')

i_a = []
for line in x.readlines():
    i_a.append(line.replace('\n', ''))

numbers_to_draw_text = i_a[0].split(',')
numbers_to_draw = []

for item in numbers_to_draw_text:
    numbers_to_draw.append(int(item))

scorecards = []
line_number = 1

while line_number < len(i_a) - 1:
    while i_a[line_number].strip() == '':
        line_number += 1
    card = []
    for i in range(5):
        text_array = i_a[line_number].strip()\
            .replace('  ', ' ')\
            .replace('\n', '')\
            .split(' ')
        row = list(map(lambda x: int(x), text_array))

        card.append(row)
        line_number += 1

    scorecards.append(card)
    
print(scorecards)