import pprint


def recipe(ingredients):
    return {'ingredient_name': ingredients.split(' | ')[0],
            'quantity': int(ingredients.split(' | ')[1]),
            'measure': ingredients.split(' | ')[2].strip()}


def read_file(file: str) -> dict:
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        for string in f:
            dish_name = string.strip()
            quantity = int(f.readline().strip())
            cook_book[dish_name] = []
            for ingredients in range(quantity):
                cook_book[dish_name].append(recipe(f.readline()))
            f.readline()
        return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int = 1) -> dict:
    list_by_dishes = {}
    for dish in dishes:
        for ingredients in read_file('recipes.txt')[dish]:
            ingredient = ingredients['ingredient_name']
            quantity = ingredients['quantity'] if ingredient not in list_by_dishes else ingredients['quantity'] + list_by_dishes[ingredient]['quantity']
            measure = ingredients['measure']
            list_by_dishes[ingredient] = {'quantity': quantity, 'measure': measure}
    for val in list_by_dishes.values():
        val['quantity'] *= person_count
    return list_by_dishes


dishes = ['Омлет', 'Фахитос', 'Омлет']
pprint.pprint(get_shop_list_by_dishes(dishes, 2))
