import numpy as np

from utils.readers import reader_split_by_exp


def rotate_beacons(beacons):
    rot_x = np.array(
        [
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[1, 0, 0], [0, 0, -1], [0, 1, 0]],
            [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
            [[1, 0, 0], [0, 0, 1], [0, -1, 0]],
        ]
    )
    rot_y = np.array(
        [
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
            [[0, 0, 1], [0, 1, 0], [-1, 0, 0]],
            [[-1, 0, 0], [0, 1, 0], [0, 0, -1]],
            [[0, 0, -1], [0, 1, 0], [1, 0, 0]],
        ]
    )
    rot_z = np.array(
        [
            [[0, -1, 0], [1, 0, 0], [0, 0, 1]],
            [[0, 1, 0], [-1, 0, 0], [0, 0, 1]],
        ]
    )
    rot_matrices = []
    for i1 in range(rot_x.shape[0]):
        for i2 in range(rot_y.shape[0]):
            new_mat = (rot_x[i1] @ rot_y[i2] @ beacons.transpose()).transpose()
            rot_matrices.append(new_mat)

        for i2 in range(rot_z.shape[0]):
            new_mat = (rot_x[i1] @ rot_z[i2] @ beacons.transpose()).transpose()
            rot_matrices.append(new_mat)

    return rot_matrices


def is_overlap(origin_beacons, rot_variant, delta):
    n_overlap = 0
    for beacon in rot_variant:
        new_vec = tuple(np.array(beacon) + delta)
        if new_vec in origin_beacons:
            n_overlap += 1
            if n_overlap > 11:
                return True

    return False


def parse_scanner_reports(input):
    reports = {}
    scanner_idx = 0
    for report in input:
        beacons = []
        for line in report:
            beacons.append([int(coord) for coord in line.split(",")])

        rotated_beacons = rotate_beacons(np.array(beacons))
        scanner = {}
        for idx, rot_variant in enumerate(rotated_beacons):
            scanner[idx] = set([tuple(beacon) for beacon in rot_variant])

        reports[scanner_idx] = scanner
        scanner_idx += 1

    return reports


def update_beacons(scanner_reports, scanner, rot_variant, delta):
    new_set = set()
    for beacon in rot_variant:
        new_set.add(tuple(np.array(beacon) + delta))

    scanner_reports[scanner][0] = new_set


def find_delta(origin_scanner, scanner, scanner_reports):
    for rot_variant in scanner_reports[scanner].values():
        delta_count = {}
        for origin_beacon in scanner_reports[origin_scanner][0]:
            for beacon in rot_variant:
                delta = np.array(origin_beacon) - np.array(beacon)
                delta_tup = tuple(delta)
                if delta_tup in delta_count:
                    delta_count[delta_tup] += 1
                    if delta_count[delta_tup] > 11:
                        update_beacons(scanner_reports, scanner, rot_variant, delta)
                        return delta
                else:
                    delta_count[delta_tup] = 1
    return None


def determine_scanner_pos(scanner_reports):
    solved_scanners = [0]
    queued_scanners = [0]
    scanner_pos = [np.array([0, 0, 0])]

    while len(solved_scanners) < len(scanner_reports):
        origin_scanner = queued_scanners.pop()
        for scanner in scanner_reports.keys():
            if scanner not in solved_scanners:
                delta = find_delta(origin_scanner, scanner, scanner_reports)
                if delta is not None:
                    solved_scanners.append(scanner)
                    queued_scanners.append(scanner)
                    scanner_pos.append(delta)

    return scanner_pos


def solution_1(input):
    scanner_reports = parse_scanner_reports(input)
    determine_scanner_pos(scanner_reports)

    comb_set = set()
    for report in scanner_reports.values():
        comb_set = comb_set.union(report[0])
    return len(comb_set)


def solution_2(input):
    scanner_reports = parse_scanner_reports(input)
    positions = determine_scanner_pos(scanner_reports)
    max_manhattan_dist = 0
    for pos1 in positions:
        for pos2 in positions:
            dist = np.absolute((pos1 - pos2)).sum()
            if dist > max_manhattan_dist:
                max_manhattan_dist = dist

    return max_manhattan_dist


if __name__ == "__main__":
    input = reader_split_by_exp("y2021/inputs/day19.txt", r"--- scanner \d+ ---")
    print(f"Answer to part 1 is: {solution_1(input)}")
    print(f"Answer to part 2 is: {solution_2(input)}")
