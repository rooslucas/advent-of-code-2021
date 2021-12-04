import numpy as np
import copy

data_input = open("input.txt", 'r')
inp = data_input.readlines()

bingo_list = inp[0].strip().split(',')

print(bingo_list)
bingo_cardss = inp[1:]

temp_list = []
bingo_cards = []
for line in bingo_cardss:
    if line != '\n':
        temp_list.append(line.strip().split())
    else:
        if temp_list != []:
            bingo_cards.append(temp_list)
            temp_list = []
print(bingo_cards)

bingo = False
bingo_card = ''
numb = ''
last_card = ''
for number in bingo_list:
    for card in bingo_cards:
        for row in card:
            if number in row:
                res = [row.index(i) for i in [number]]
                row[res[0]] = 'X'
            if row == ['X', 'X', 'X', 'X', 'X']:
                bingo = True
                bingo_card = copy.deepcopy(card)
                numb = number
                print("BINGO")
                print(number)
                card.clear()
                print(bingo_card)
                break

            for column in range(len(card)):
                cards = np.matrix(card)
                if (cards.T[column] == ['X', 'X', 'X', 'X', 'X']).all():
                    print("BINGO")
                    bingo_card = copy.deepcopy(card)
                    numb = number
                    bingo = True
                    print(number)
                    print(card)
                    card.clear()
                    break

    #     if bingo:
    #         break
    # if bingo:
    #     break

total = 0
print(numb)
print(bingo_card)
for lists in bingo_card:
    for values in lists:
        if values != 'X':
            total += int(values)
            print(total)

print(total * int(numb))

