from contents import pantry, recipes

to_buy = {}


def buying(quantities=0, items="print"):
    if items == "print":
        print(f"Items to buy {to_buy}")
    # if items not in to_buy:
    #     to_buy[items] = quantities
    # else:
    #     to_buy[items] += quantities
    to_buy[items] = to_buy.setdefault(items, 0)+quantities
    # set_default item irrutha athoda value return pannu illana new item(key) ma create pannu default aa namma
    # zero set panniruko ipo antha key illana


display_dict = {}
for index, key in enumerate(recipes):  # enumerate map la key a matum tha iterate pannum key ku oru index athuva tharu
    display_dict[str(index + 1)] = key
while True:
    print("Please enter valid choice ")
    print("-------------------------")
    for key, val in display_dict.items():
        print(f"{key} : {val}")
    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        print(f"You have selected {display_dict[choice]}")
        print("checking ingrediants .........")
        ingredients = recipes[display_dict[choice]]
        print(ingredients)
        for item, quantity in ingredients.items():
            quantity_in_pantry = pantry.get(item, 0)  # oru velai illama irrutha 0 the return agu indexing la error agum
            if quantity_in_pantry >= quantity:
                print(f"\t{item} irruku")
            else:
                print(f"\tpantry as not enough {item} ingredients to make {display_dict[choice]} ")
                print(f"\t\tyou want to buy {quantity - quantity_in_pantry}:{item} ")
                buying(quantity - quantity_in_pantry, item)
buying()
