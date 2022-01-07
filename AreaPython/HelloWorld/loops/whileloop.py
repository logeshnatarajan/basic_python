i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
exits = ["north", "south", "east", "west"]
way = ""
while way not in exits:
    way = input("enter your way ")
    if way.casefold() == "quit":
        print("you quit form game")
        break
else:
    print("glad that you out form there ")
print()
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
