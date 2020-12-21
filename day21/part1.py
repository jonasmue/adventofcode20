from common import *


if __name__ == "__main__":
    food_list = get_input()
    all_ingredients = set.union(*[item[0] for item in food_list])
    algn2ingrdnt = get_allergen_dict(food_list)
    possible_allergenic = set.union(*algn2ingrdnt.values())
    not_allergenic = all_ingredients - possible_allergenic
    
    sum = 0
    for ingredients, _ in food_list:
        for i in ingredients:
            if i in not_allergenic:
                sum += 1
    print(sum)
