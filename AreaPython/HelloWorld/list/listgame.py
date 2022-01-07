items = ["computer", "keyboard", "mouse", "laptop", "html", "bluetooth"]
orders = []
current_choice = " "
print("to exit press zero")
while current_choice != "0":
    if current_choice in "123456":
        print("you choice {}".format(current_choice))
        if int(current_choice) < len(items)+1:
            if items[int(current_choice)-1] in orders:
                orders.remove(items[int(current_choice)-1])
            else:
                orders.append(items[int(current_choice) - 1])
                print("Adding : {}".format(orders))
    # else:
    #     print("choose form the given list")
    #     for parts in items:
    #         print("{} : {}".format(items.index(parts) + 1, parts))
    else:
        print("choose from the given list")
        for index, val in enumerate(items):
            print("{1:10} : {0}".format(index+1, val))

    current_choice = input()
print("your orders : {}".format(orders))
