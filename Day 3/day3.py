x = open('input.txt', 'r')
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

new_i_a = i_a[:]

def og_rating():
    for item in new_i_a:
        for x in range(len(new_i_a[0])):
            if int(item[x]) != mc[x]:
                i_a.remove(item)
                

# og_rating()
# print(i_a)


# def result():
    # while i_a > 1:


# print(mc)
# print(i_a, lc)

print(mc, lc)

dec_mc = int(mc, 2)
dec_lc = int(lc ,2)
print(dec_mc * dec_lc)


