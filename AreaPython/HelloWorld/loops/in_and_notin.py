bird = "Golden Brown"
colour = input()
if colour in bird:
    print("{} in {}".format(colour,bird) )
else:
    print("not needed")

act = input("enter where you want to go ")
if "cinema" not in act.casefold():
    print("but i want togo for cinema")
else :
    print("super let us go for cinema")