data_input = open("input.txt", 'r')
inp = data_input.readlines()

horizontal = 0
depth = 0
for line in inp:
    line = line.strip()
    if "forward" in line:
        horizontal += int(line[-1])
    elif "down" in line:
        depth += int(line[-1])
    elif "up" in line:
        depth -= int(line[-1])

print(horizontal)
print(depth)
print(horizontal * depth)

aim = 0
horizontal2 = 0
depth2 = 0
for line in inp:
    line = line.strip()
    if "forward" in line:
        horizontal2 += int(line[-1])
        depth2 += (int(line[-1])*aim)
    elif "down" in line:
        aim += int(line[-1])
    elif "up" in line:
        aim -= int(line[-1])

print(horizontal2)
print(depth2)
print(horizontal2 * depth2)
