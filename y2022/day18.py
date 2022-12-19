from utils.readers import reader_split_by_line


def planes_from_cube(cube):
    # below
    planes = [
        (
            (cube[0], cube[1], cube[2]),
            (cube[0] + 1, cube[1] + 1, cube[2]),
        )
    ]
    # above
    planes.append(
        (
            (cube[0], cube[1], cube[2] + 1),
            (cube[0] + 1, cube[1] + 1, cube[2] + 1),
        )
    )
    # front
    planes.append(
        (
            (cube[0], cube[1], cube[2]),
            (cube[0] + 1, cube[1], cube[2] + 1),
        )
    )
    # back
    planes.append(
        (
            (cube[0], cube[1] + 1, cube[2]),
            (cube[0] + 1, cube[1] + 1, cube[2] + 1),
        )
    )
    # left
    planes.append(
        (
            (cube[0], cube[1], cube[2]),
            (cube[0], cube[1] + 1, cube[2] + 1),
        )
    )
    # right
    planes.append(
        (
            (cube[0] + 1, cube[1], cube[2]),
            (cube[0] + 1, cube[1] + 1, cube[2] + 1),
        )
    )
    return planes


def find_droplet_surface_planes(droplets):
    surface_planes = set()
    for droplet in droplets:
        droplet_planes = planes_from_cube(droplet)
        for plane in droplet_planes:
            if plane in surface_planes:
                surface_planes.remove(plane)
            else:
                surface_planes.add(plane)

    return surface_planes


def find_min_max(droplets):
    x_min, x_max = droplets[0][0], droplets[0][0]
    y_min, y_max = droplets[0][1], droplets[0][1]
    z_min, z_max = droplets[0][2], droplets[0][2]
    for droplet in droplets:
        if droplet[0] < x_min:
            x_min = droplet[0]
        elif droplet[0] > x_max:
            x_max = droplet[0]

        if droplet[1] < y_min:
            y_min = droplet[1]
        elif droplet[1] > y_max:
            y_max = droplet[1]

        if droplet[2] < z_min:
            z_min = droplet[2]
        elif droplet[2] > z_max:
            z_max = droplet[2]

    return x_min, x_max, y_min, y_max, z_min, z_max


def get_neighbour_cubes(cube):
    return [
        (cube[0] + 1, cube[1], cube[2]),
        (cube[0] - 1, cube[1], cube[2]),
        (cube[0], cube[1] + 1, cube[2]),
        (cube[0], cube[1] - 1, cube[2]),
        (cube[0], cube[1], cube[2] + 1),
        (cube[0], cube[1], cube[2] - 1),
    ]


def is_air_pocket(cube, droplet_cubes, x_min, x_max, y_min, y_max, z_min, z_max):
    if cube in droplet_cubes:
        return False

    neighbour_cubes = get_neighbour_cubes(cube)
    old_neighbours = set(neighbour_cubes)
    while len(neighbour_cubes) > 0:
        neighbour = neighbour_cubes.pop()
        if (
            neighbour[0] < x_min
            or neighbour[0] > x_max
            or neighbour[1] < y_min
            or neighbour[1] > y_max
            or neighbour[2] < z_min
            or neighbour[2] > z_max
        ):
            return False

        if neighbour not in droplet_cubes:
            new_neighbours = get_neighbour_cubes(neighbour)
            for new_neighbour in new_neighbours:
                if new_neighbour not in old_neighbours:
                    neighbour_cubes.append(new_neighbour)
                    old_neighbours.add(new_neighbour)

    return True


def solution_1(input_path):
    inp = reader_split_by_line(input_path)
    droplets = [tuple([int(c) for c in line.split(",")]) for line in inp]
    return len(find_droplet_surface_planes(droplets))


def solution_2(input_path):
    inp = reader_split_by_line(input_path)
    droplets = [tuple([int(c) for c in line.split(",")]) for line in inp]
    surface_planes = find_droplet_surface_planes(droplets)

    x_min, x_max, y_min, y_max, z_min, z_max = find_min_max(droplets)
    droplet_cube_set = set(droplets)

    potential_air_pocket_cubes = []
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                potential_air_pocket_cubes.append((x, y, z))

    verified_air_pockets = []
    for cube in potential_air_pocket_cubes:
        if is_air_pocket(
            cube, droplet_cube_set, x_min, x_max, y_min, y_max, z_min, z_max
        ):
            verified_air_pockets.append(cube)

    # Remove surface planes not on exterior
    for cube in verified_air_pockets:
        pocket_planes = planes_from_cube(cube)
        for plane in pocket_planes:
            if plane in surface_planes:
                surface_planes.remove(plane)

    return len(surface_planes)


if __name__ == "__main__":
    input_path = "y2022/inputs/day18.txt"
    print(f"Answer to part 1 is: {solution_1(input_path)}")
    print(f"Answer to part 2 is: {solution_2(input_path)}")
