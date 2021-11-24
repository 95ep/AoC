import re


def load_input(path):
    with open(path) as f:
        content = f.read()

    all_entries = re.findall(r".+ \(contains .+\)\n?", content)
    all_ingredients = []
    all_allergens = []
    for entry in all_entries:
        m = re.match("(.+) \(contains (.+)\)\n?", entry)
        ingredients = m.group(1)
        allergens = m.group(2)
        all_ingredients.append(re.findall("[a-z]+", ingredients))
        all_allergens.append(re.findall("[a-z]+", allergens))

    return all_ingredients, all_allergens


def find_potential_allergen_ingredients(all_ingredients, all_allergens):
    allergens_to_ingredients_dict = {}
    for ingredients, allergens in zip(all_ingredients, all_allergens):
        for allergen in allergens:
            if allergen not in allergens_to_ingredients_dict:
                allergens_to_ingredients_dict[allergen] = ingredients.copy()
            else:
                allergens_to_ingredients_dict[allergen].append(ingredients.copy())

    for allergen, ingredients_lists in allergens_to_ingredients_dict.items():
        n_lists = len(ingredients_lists)
        tmp_list = []
        for ingredient in ingredients_lists[0]:
            in_all = True
            for i in range(1,n_lists):
                if ingredient not in ingredients_lists[i]:
                    in_all = False
                    break

            if in_all:
                tmp_list.append(ingredient)

        allergens_to_ingredients_dict[allergen] = tmp_list

    return allergens_to_ingredients_dict



ingredients, allergens = load_input('inputs/day21.txt')
print(ingredients)
print(allergens)
di = find_potential_allergen_ingredients(ingredients,allergens)
print(di)
