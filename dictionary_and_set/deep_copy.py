import copy

animals2 = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}
# this is shallow copy
# an = animals2.copy()

# this is deep copy
an = copy.deepcopy(animals2)

an["teddy"].append("toy")
print(animals2["teddy"])
print(an["teddy"])

# to conform they are different
print(id(animals2["teddy"]))
print(id(an["teddy"]))

