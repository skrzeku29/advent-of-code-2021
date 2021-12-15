import re
from typing import Text

def gen_array_of_data():
    with open("test-data.txt") as data:
        # data = list(filter(re.compile("[0-9]+").groups, data.read().split("\n")))
        data = data.read().split("\n")

    return data

# x1 y1 x2 y2

data = gen_array_of_data()
# print(data[0])
# print(re.compile("[0-9]+").match(data[0]))

coords = []
map_repres = [[0]*10]*10
for item in data:
    matches = re.findall("[0-9]+", item)
    for i in range(0, len(matches), 4):
        coords.append(matches[i:i+4])

# print(coords)
# print(map_repres)

def plot_cord(map_repres, coord):
    x1 = int(coord[0])
    y1 = int(coord[1])
    x2 = int(coord[2])
    y2 = int(coord[3])

    tx=abs(x1-x2)
    ty=abs(y1-y2)
    smaller_x = min(x1, x2)
    smaller_y = min(y1, y2)


    if x1 == x2:
        print("doing that")
        for i in range(smaller_y, smaller_y+ty+1, 1):
            map_repres[x1][i]+=1
    else:

        # WHAT IN DA DUCK is going on with this 
        for i in range(smaller_x, smaller_x+tx+1, 1):
            # print(map_repres[y1][i])
            map_repres[9][i]=map_repres[9][i]+1
            # print(map_repres[y1][i])

    # print(map_repres)

    return map_repres

    
# for coord in coords:
#     map_repres = plot_cord(map_repres, coord)
map_repres = plot_cord(map_repres, coords[0])
# print(map_repres)

for ma in map_repres:
    print(ma)