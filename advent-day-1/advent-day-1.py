import numpy as np
# part 1
data_input = open("input.txt", 'r')
inp = data_input.readlines()

prev = 1000
count = 0

for line in range(len(inp)):
    inp[line] = int(inp[line].strip())
    line = inp[line]
    if line > prev:
        count += 1
    prev = line

print(count)

# part 2
sliding_window = []
count2 = 0
index1 = 0
index2 = 1
index3 = 2
i = True

while i:
    if index3 < len(inp):
        sliding_window.append(inp[index1] + inp[index2] + inp[index3])
        index1 += 1
        index2 += 1
        index3 += 1
    else:
        i = False

count3 = 0
prev_slide = 1000
for slide in sliding_window:
    if slide > prev_slide:
        count3 += 1
    prev_slide = slide

print(count3)
