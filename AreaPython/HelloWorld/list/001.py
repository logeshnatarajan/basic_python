items = ["milk", "potato", "tomato", "carrotandbean", "curry"]
for item in items:
    print(item)
print()
for item in items:
    if item != "carrotandbean":
        print(item)
print()
for item in items:
    if item == "carrotandbean":
        continue
    print(item)
