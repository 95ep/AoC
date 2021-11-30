import re
import numpy as np


def load_input(path):
    with open(path) as f:
        tiles = {}
        tmp = []
        heading_exp = re.compile("Tile (\d{4}):")
        heading = re.findall(heading_exp,f.readline())[0]
        for line in f:
            if line == '\n':
                continue
            tmp_heading = re.findall(heading_exp, line)
            if tmp_heading:
                tiles[heading] = np.array(tmp)
                heading = tmp_heading[0]
                tmp = []
            else:
                tmp.append(list(line.strip('\n')))

        tiles[heading] = np.array(tmp)

    return tiles

def is_neighbour(tile1, tile2):
    borders_1 =  [tile1[0,:], tile1[:,0], tile1[-1,:], tile1[:,-1] ]
    borders_2 =  [tile2[0,:], tile2[:,0], tile2[-1,:], tile2[:,-1] ]
    for border_1 in borders_1:
        for border_2 in borders_2:
            if (border_1 == border_2).all() or (border_1 == np.flip(border_2)).all():
                return True

    return False

def find_corners(tiles):
    potential_corners = tiles.copy()
    actual_corners = []
    while len(potential_corners) > 0:
        id1, tile1 = potential_corners.popitem()
        n_neighbours = 0
        for id2, tile2 in tiles.items():
            if id1 == id2:
                continue
            if is_neighbour(tile1, tile2):
                n_neighbours += 1

            if n_neighbours > 2:
                break

        if n_neighbours > 2 and n_neighbours < 5:
            pass
        elif n_neighbours == 2:
            actual_corners.append(int(id1))
        else:
            raise ValueError(f"N neighbours_invalid: {n_neighbours}")
    return actual_corners



tiles = load_input('inputs/day20.txt')
corner_ids = find_corners(tiles)
print(f"Product of corner IDs is: {np.prod(corner_ids)}")