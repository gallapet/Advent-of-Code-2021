x = open('test.txt', 'r')
i_a = []
for line in x.readlines():
    i_a.append(line.replace('\n', ''))

# test = 5 long
# input = 12 long

print(i_a)
mc = [0] * len(i_a[0])
lc = [0] * len(i_a[0])

def get_most_common_digit(column):
    ones = 0
    zeros = 0
    for item in i_a:
        if int(item[column]) == 1:
            ones += 1
        else:
            zeros += 1            
    if ones > zeros:
        return 1
    return 0

mc = ''
lc = ''

for i in range(len(i_a[0])):
    answer = get_most_common_digit(i)
    mc = mc + str(answer)
    lc = lc + str(1 - answer) 

# new_i_a = i_a[:]

# Part2
def removeRowsByColumnValue(column, value):
    new_i_a = []
    for item in i_a:
        if item[column] == value:
            new_i_a.append(item)
    return new_i_a

def og_rating(digitLength):
    for column in range(digitLength):
        mc = get_most_common_digit(column)
        i_a = removeRowsByColumnValue(column, mc)



                

og_rating(len(i_a[0]))
print(i_a)


# def result():
    # while i_a > 1:


# print(mc)
# print(i_a, lc)

dec_mc = int("".join(str(i) for i in mc), 2)
dec_lc = int("".join(str(i) for i in lc), 2)
print(dec_mc * dec_lc)


