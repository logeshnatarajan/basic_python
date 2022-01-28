from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """
    copy a dictionary
    :param d: dictionary
    :return: copy of d
    """
    new_dict = {}
   # print(d)
    for key, value in d.items():
        # print(key)
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
