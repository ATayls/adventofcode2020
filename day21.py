with open(r"data/day21_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]

def parse_input(puzzle_input):
    foods = []
    for line in puzzle_input:
        ingredients, allergens = line.split("(contains ")
        allergens, _ = allergens.split(")")
        ingredients = [x for x in ingredients.split(" ") if x is not ""]
        allergens = [x for x in allergens.split(", ") if x is not ""]
        foods.append((ingredients, allergens))
    return foods

def get_allergen_sets(foods):
    allergen_sets = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in allergen_sets:
                allergen_sets[allergen] = set(ingredients)
            else:
                allergen_sets[allergen] = allergen_sets[allergen].intersection(set(ingredients))
    return allergen_sets

example = [
"mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
"trh fvjkl sbzzf mxmxvkd (contains dairy)",
"sqjhc fvjkl (contains soy)",
"sqjhc mxmxvkd sbzzf (contains fish)",
]

foods = parse_input(puzzle_input)
allergen_sets = get_allergen_sets(foods)

all_ingredients = [y for x in foods for y in x[0]]
inert_ingredients = set(all_ingredients) - set([y for x in allergen_sets.values() for y in x])
answer = 0
for ing in inert_ingredients:
    answer += all_ingredients.count(ing)
print(answer)

out_dict = {}
found = []
while sorted(allergen_sets.keys()) != sorted(out_dict.keys()):
    for allergen, ing_list in allergen_sets.items():
        ing_list = list(set(ing_list)-set(found))
        if len(ing_list) == 1:
            out_dict[allergen] = ing_list[0]
            found.append(ing_list[0])

answer = ""
for i in sorted(out_dict.keys()):
    if answer != "":
        answer += ","
    answer += out_dict[i]
print(answer)