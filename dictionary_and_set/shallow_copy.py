animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly"
}
thing = animals
animals["teddy"] = "toy"
print(thing["teddy"])
print()
second = animals.copy()
animals["teddy"] = "podu"
print(second["teddy"])
print(animals["teddy"])

animals2 = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
}
an = animals2
an["teddy"].append("toy")
print(animals2["teddy"])
print(an["teddy"])
