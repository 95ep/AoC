import numpy as np
import re

def load_input(path):
    with open(path) as f:
        tiles_list = []
        headings_list = []
        tmp = []
        heading_exp = re.compile("Tile (\d{4}):")
        heading = re.findall(heading_exp,f.readline())[0]
        for line in f:
            if line == '\n':
                continue
            tmp_heading = re.findall(heading_exp, line)
            if tmp_heading:
                tiles_list.append(tmp)
                headings_list.append(heading)
                heading = tmp_heading[0]
                tmp = []
            else:
                tmp.append(list(line.strip('\n')))

        tiles_list.append(tmp)
        headings_list.append(heading)

    return np.array(tiles_list), headings_list


def find_matching_borders(all_tiles):
    n_tiles = len(all_tiles)
    # List (nested to hold all matches) One list per tile and side.
    # Format of entry (matching tile, matching side, if flipped)
    matches = [[[] for _ in range(4)] for _ in range(n_tiles)]
    for i1 in range(n_tiles):
        for i2 in range(i1+1, n_tiles):
            local_matches = check_borders(all_tiles[i1], all_tiles[i2])
            for m in local_matches:
                matches[i1][m[0]].append((i2, m[1], m[2]))
                matches[i2][m[1]].append((i1, m[0], m[2]))

    return matches

def check_borders(tile1, tile2):
    matches = []
    borders_1 = [tile1[:,0], tile1[:,1], tile1[0,:], tile1[1,:]]
    borders_2 = [tile2[:,0], tile2[:,1], tile2[0,:], tile2[1,:]]

    for i1, border1 in enumerate(borders_1):
        for i2, border2 in enumerate(borders_2):
            if (border1 == border2).all():
                # Format match (side on tile1, side on tile2, if flipped)
                matches.append((i1, i2, False))

            if (border1 == np.flip(border2)).all():
                # Format match (side on tile1, side on tile2, if flipped)
                matches.append((i1, i2, True))

    return matches

tiles, headings = load_input('inputs/day20.txt')
print(len(tiles))
print(headings)
all_matches = find_matching_borders(tiles)
for m in all_matches:
    print(m)