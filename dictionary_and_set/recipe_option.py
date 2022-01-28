recipe_tuples = {"Chicken and chips": [
    ("chicken", 100),
    ("potatoes", 3),
    ("salt", 1),
    ("malt vinegar", 5),
],
}
recipe_dicts = {"Chicken and chips": {
    "chicken": 100,
    "potatoes": 3,
    "salt": 1,
    "malt vinegar": 5,
}
}
for recipe, ingredient in recipe_tuples.items():
    print(f"ingredient for {recipe}")
    for item, quantity in ingredient:
        print(f"{item} : {quantity}")
for recipe, ingredient in recipe_dicts.items():
    print(f"ingredient for {recipe}")
    for item, quantity in ingredient.items():
        print(f"{item} : {quantity}")
