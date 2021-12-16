def load_input(path):
    signals = []
    with open(path) as f:
        for line in f:
            signal_patterns, outputs = line.rstrip().split("|")
            signals.append((signal_patterns.split(), outputs.split()))

    return signals


def count_unique_segments_in_output(signals, nr_segments):
    counter = 0
    for _, outputs in signals:
        for output in outputs:
            if len(output) == nr_segments:
                counter += 1
    return counter


def get_wire_per_frequency(frequency_per_wire, desired_frequency):
    wires_matching_freq = []
    for wire, freq in frequency_per_wire.items():
        if freq == desired_frequency:
            wires_matching_freq.append(wire)

    return wires_matching_freq


def resolve_wires_to_segments(patterns):
    # 0 uses 6 segments
    # 1 uses 2 segments
    # 2 uses 5 segments
    # 3 uses 5 segments
    # 4 uses 4 segments
    # 5 uses 5 segments
    # 6 uses 6 segments
    # 7 uses 3 segments
    # 8 uses 7 segments
    # 9 uses 6 segments
    frequency_per_wire = calc_frequency_per_wire(patterns)
    wires_to_segments = {}

    # Find mapping based on freqency
    for wire, freq in frequency_per_wire.items():
        if freq == 4:
            wires_to_segments[wire] = "e"
        elif freq == 6:
            wires_to_segments[wire] = "b"
        elif freq == 9:
            wires_to_segments[wire] = "f"

    n_segments_to_number = {2: 1, 3: 7, 4: 4, 7: 8}
    number_to_patterns = {}
    for pattern in patterns:
        for n_segments, number in n_segments_to_number.items():
            if len(pattern) == n_segments:
                number_to_patterns[number] = pattern

    # Find wire for segment 'd' & 'g'
    wire_with_freq_7 = get_wire_per_frequency(frequency_per_wire, 7)
    for wire in wire_with_freq_7:
        if wire in number_to_patterns[8] and wire not in number_to_patterns[4]:
            wires_to_segments[wire] = "g"
        else:
            wires_to_segments[wire] = "d"

    # Find wire for segment 'a' & 'c'
    wire_with_freq_8 = get_wire_per_frequency(frequency_per_wire, 8)
    for wire in wire_with_freq_8:
        if wire in number_to_patterns[7] and wire not in number_to_patterns[1]:
            wires_to_segments[wire] = "a"
        else:
            wires_to_segments[wire] = "c"

    return wires_to_segments


def calc_output(output, wires_to_segments):
    number_to_segments = {
        0: {"a", "b", "c", "e", "f", "g"},
        1: {"c", "f"},
        2: {"a", "c", "d", "e", "g"},
        3: {"a", "c", "d", "f", "g"},
        4: {"b", "c", "d", "f"},
        5: {"a", "b", "d", "f", "g"},
        6: {"a", "b", "d", "e", "f", "g"},
        7: {"a", "c", "f"},
        8: {"a", "b", "c", "d", "e", "f", "g"},
        9: {"a", "b", "c", "d", "f", "g"},
    }
    digits = []
    for digit in output:
        digit_set = set()
        for wire in digit:
            digit_set.add(wires_to_segments[wire])
        for number, segments_set in number_to_segments.items():
            if digit_set == segments_set:
                digits.append(number)
                break

    return digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]


def calc_frequency_per_wire(patterns):
    frequency_per_wire = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
    }
    for pattern in patterns:
        for wire in pattern:
            frequency_per_wire[wire] += 1

    return frequency_per_wire


def calc_output_sum(signals):
    sum = 0
    for signal in signals:
        wires_to_segments = resolve_wires_to_segments(signal[0])
        sum += calc_output(signal[1], wires_to_segments)

    return sum


signals = load_input("2021/inputs/day08.txt")
nr_ones = count_unique_segments_in_output(signals, 2)
nr_fours = count_unique_segments_in_output(signals, 4)
nr_sevens = count_unique_segments_in_output(signals, 3)
nr_eights = count_unique_segments_in_output(signals, 7)
print(f"The unique digits appears {nr_ones + nr_fours + nr_sevens + nr_eights} times")

print(f"Sum of all output values are: {calc_output_sum(signals)}")
