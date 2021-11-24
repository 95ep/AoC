def memory_game(starting_numbers):
    spoken_numbers = {}
    last_number = None
    for idx, numb in enumerate(starting_numbers):
        if last_number is not None:
            spoken_numbers[str(last_number)] = idx - 1
        last_number = numb

    for idx in range(len(spoken_numbers), 30000000-1):
        if idx % 10**6 == 0:
            print(f"Progress, loop {idx}")
        if str(last_number) in spoken_numbers.keys():
            new_numb = idx - spoken_numbers[str(last_number)]
        else:
            new_numb = 0

        spoken_numbers[str(last_number)] = idx
        last_number = new_numb

    return last_number



start_num = [19,0,5,1,10,13]
print(memory_game(start_num))