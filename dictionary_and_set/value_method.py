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

k = d.keys()
print(k)
v = d.values()
print(v)
d[10] = "ten"
print(v)
print(k)
print("four" in v)
print("eleven" in v)
print(11 in k)
print(7 in k)
for key,value in d.items():
    if value == "four":
        print(f"key for value:{value} is {key}")
