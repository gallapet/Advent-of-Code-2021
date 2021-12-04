from pprint import pprint as pp

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
        


print('')
print(scorecard_numbers)
print('')