items = ["milk", "potato", "tomato", "carrotandbean", "curry"]
# illerating over thelist
for item in items:
    print(item)
print()
# checking elements in list
for item in items:
    if item != "carrotandbean":
        print(item)
print()
for item in items:
    if item == "carrotandbean":
        continue
    print(item)
