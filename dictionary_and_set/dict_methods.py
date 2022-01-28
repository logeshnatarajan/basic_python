d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict)
keys = d.keys()
print(keys)
for item in d:
    print(item)
for item in d.keys():
    print(item)
