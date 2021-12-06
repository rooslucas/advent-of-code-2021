import pandas as pd
import numpy as np

raster = pd.DataFrame(np.random.rand(1000, 1000), columns=np.arange(0, 1000, 1), )
for column in raster:
    raster[column] = 0
print(raster)


class Coordinates:
    # data members of class
    hline = False
    vline = False

    # class default constructor
    def __init__(self, xy1, xy2):
        self.x1 = int(xy1[0])
        self.x2 = int(xy2[0])
        self.y1 = int(xy1[1])
        self.y2 = int(xy2[1])

    # user defined function of class
    def overlap(self):
        if self.x1 == self.x2:
            self.vline = True
        elif self.y1 == self.y2:
            self.hline = True


with open("input.txt", 'r') as f:
    inp = f.readlines()
    for line in range(len(inp)):
        cords = list(inp[line].strip().split(' '))
        cords.remove('->')
        for val in range(len(cords)):
            cords[val] = cords[val].split(',')
        inp[line] = Coordinates(cords[0], cords[1])
        inp[line].overlap()

for cords in inp:
    if cords.hline:
        for key in range(cords.x1, cords.x2+1):
            raster.iat[cords.y1, key] += 1
            print(raster.iat[cords.y1, key])

    elif cords.vline:
        for key in range(cords.y1, cords.y2+1):
            raster.iat[key, cords.x1] += 1


print(raster)

count = 0
for column in raster:
    for row in raster[column]:
        if raster.loc[row, column] >= 2:
            count += 1

print(count)
