def recipe(ingredients):
    return {'ingredient_name': ingredients.split(' | ')[0],
            'quantity': int(ingredients.split(' | ')[1]),
            'measure': ingredients.split(' | ')[2].strip()}


def read_file(file:str):
    cook_book ={}
    with open(file, encoding='utf-8') as f:
        for string in f:  # запустили цикл, который читает строки
            dish_name = string.strip()  # первая строка, название блюда, получили, сохранили в переменную
            quantity = int(f.readline().strip())  # вторая строка, получили число строк рецепта, сохранили
            cook_book[dish_name] = []
            for ingredients in range(quantity):
                cook_book[dish_name].append(recipe(f.readline()))
            f.readline()
        return cook_book


import pprint
for dis, rec in read_file('recipes.txt').items():
    pprint.pprint(dis)
    pprint.pprint(rec)