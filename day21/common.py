def get_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        food_list = []
        for line in lines:
            split = line.split("(")
            ingredients = set(split[0].split())
            allergens = set(split[1][9:-1].split(", "))
            food_list.append((ingredients, allergens))
        return food_list


def get_allergen_dict(food_list):
    algn2ingrdnt = {}
    for ingredients, allergens in food_list:
        for a in allergens:
            if not a in algn2ingrdnt.keys():
                algn2ingrdnt[a] = ingredients
            else:
                algn2ingrdnt[a] = algn2ingrdnt[a].intersection(ingredients)
    return algn2ingrdnt
