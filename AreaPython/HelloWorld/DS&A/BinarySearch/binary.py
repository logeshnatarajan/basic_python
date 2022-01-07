tofind = int(input("enter the number between 1 - 1000 "))
low = 1
high = 1000
while True:
    my_guess = low + (high - low) // 2  # oru "/" na float la result varu itha rendu "//" na int la answer varu
    print("its my guess : {} type higher if my guess higher or lower when lower and crt when crt".format(my_guess))
    guess = input()
    if guess.casefold() == "higher":
        low = my_guess
    elif guess.casefold() == "lower":
        high = my_guess
        pass  # oru block la onnuma illama irruka kudathu atleast pass achu irrukanu
    elif guess.casefold() == "crt":
        print("super I guess right atlast")
        break
    else:
        print("Please enter 'higher' or 'lower' or 'crt'")
