x = open('test.txt', 'r')

i_a = []
for line in x.readlines():
    i_a.append(line.replace('\n', ''))

numbers_to_draw_text = i_a[0].split(',')
numbers_to_draw = []

for item in numbers_to_draw_text:
    numbers_to_draw.append(int(item))

scorecards = []
scores = []
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
    scores.append(0)

def mark_card(card, number):
    for row in range(5):
        for column in range(5):
            if card[row][column] == number:
                card[row][column] = None
                return

def get_card_total(card):
    score = 0
    for row in card:
        for item in row:
            if item is not None:
                score += item
    return score

def find_winning_card(card):
    for row in range(5):
        count_row = 0
        count_column = 0
        for column in range(5):
            if card[row][column] == None:
                count_row += 1
            if card[column][row] == None:
                count_column += 1
        if count_column == 5 or count_row == 5:
            return True
    return False

winning_card_found = False
last_winning_score = 0
for number in numbers_to_draw:
    print('')
    print(f"Number drawn: {number}")
    number_of_card = 0
    for card in scorecards:
        mark_card(card, number)
        score = get_card_total(card)
        winning_card = find_winning_card(card)
        print(number_of_card + 1, score, winning_card)

        if winning_card and scores[number_of_card] == 0:
            print(f"Card {number_of_card + 1} wins now")
            scores[number_of_card] = score * number
            last_winning_score = score * number
            winning_card_found = True
        
        number_of_card += 1

        # if winning_card_found:
        #     break

print(last_winning_score)