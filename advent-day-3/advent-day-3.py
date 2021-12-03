import pandas as pd
data_input = open("input.txt", 'r')
inp_frame = pd.DataFrame(columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

inp = data_input.readlines()
for line in inp:
    line_row = pd.Series(list(line.strip()), index=inp_frame.columns)
    inp_frame = inp_frame.append(line_row, ignore_index=True)

epsilon = []
gamma = []
for number in inp_frame:
    inp_frame = inp_frame.astype({number: int})
    if int(inp_frame[number].sum()) >= (len(inp_frame) / 2):
        gamma.append("1")
        epsilon.append("0")
    else:
        gamma.append("0")
        epsilon.append("1")
#
# print(''.join(gamma))
# print(''.join(epsilon))
#
# print(int(''.join(gamma), 2))
# print(int(''.join(epsilon), 2))
# print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
co2 = []
o2 = []
gamma_frame = inp_frame
epsilon_frame = inp_frame

for number in inp_frame:
    gamma_frame = gamma_frame.astype({number: int})
    if int(gamma_frame[number].sum()) >= (len(gamma_frame) / 2):
        o2.append(1)
    else:
        o2.append(0)

    if len(gamma_frame) > 1:
        for r in range(len(gamma_frame)):
            row = gamma_frame.at[r, number]
            if row != o2[int(number)]:
                samma_frame = gamma_frame.drop([r])
                if len(samma_frame) > 0:
                    gamma_frame = samma_frame
    gamma_frame = gamma_frame.reset_index(drop=True)

    epsilon_frame = epsilon_frame.astype({number: int})
    if int(epsilon_frame[number].sum()) >= (len(epsilon_frame) / 2):
        co2.append(0)
    else:
        co2.append(1)

    if len(epsilon_frame) > 1:
        for r in range(len(epsilon_frame)):
            row = epsilon_frame.at[r, number]
            if row != co2[int(number)]:
                sepsilon_frame = epsilon_frame.drop([r])
                if len(sepsilon_frame) > 0:
                    epsilon_frame = sepsilon_frame
    epsilon_frame = epsilon_frame.reset_index(drop=True)

print("gamma")
print(gamma_frame)
oo2 = int("110000010001", 2)
print("epsilon")
print(epsilon_frame)
coo2 = int("000100000001", 2)
print(oo2*coo2)

