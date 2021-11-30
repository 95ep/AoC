import re


def load_input(path):
    with open(path) as f:
        content = f.read()

    all_entries = re.findall(r".+ \(contains .+\)\n?", content)
    foods_list = []
    for entry in all_entries:
        m = re.match("(.+) \(contains (.+)\)\n?", entry)
        ingredients = m.group(1)
        allergens = m.group(2)
        foods_list.append(
            (re.findall("[a-z]+", ingredients), re.findall("[a-z]+", allergens))
        )

    return foods_list


def find_all_allergens(foods_list):
    all_allergens = []
    for _, allergens in foods_list:
        for allergen in allergens:
            if allergen not in all_allergens:
                all_allergens.append(allergen)

    return all_allergens


def resolve_allergens(all_allergens, foods_list):
    solved_allergens = {}
    while len(all_allergens) > 0:
        allergen = all_allergens.pop()
        possible_ingredients = []
        # Add all possible ingredients that could contain allergen
        for ingredients, allergens in foods_list:

            if allergen in allergens:
                possible_ingredients.append(
                    [
                        ingredient
                        for ingredient in ingredients
                        if ingredient not in solved_allergens.values()
                    ]
                )

        common_ingredients = []

        for ingredient in possible_ingredients[0]:
            is_common = True
            for ingredients in possible_ingredients:
                if ingredient not in ingredients:
                    is_common = False
                    break
            if is_common:
                common_ingredients.append(ingredient)

        if len(common_ingredients) == 1:
            solved_allergens[allergen] = common_ingredients[0]
        else:
            all_allergens.insert(0, allergen)

    return solved_allergens


def count_safe_foods(foods_list, solved_allergens):
    counter = 0
    for ingredients, _ in foods_list:
        for ingredient in ingredients:
            if ingredient not in solved_allergens.values():
                counter += 1

    return counter


foods_list = load_input("inputs/day21.txt")
allergens = find_all_allergens(foods_list)
solved_allergens = resolve_allergens(allergens, foods_list)

print(f"Number of safe foods: {count_safe_foods(foods_list, solved_allergens)}")
