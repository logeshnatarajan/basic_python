import random

num = random.randint(1, 10)
print(num)
incoming = int(input("enter the number between i to 10 "))
while True:
    if incoming == num:
        print("Well Done you guessed it")
        break
    if incoming == 0:
        print("you quit so game over")
        break
    else:
        if incoming < num :
            print("guess higher")
            incoming = int(input("enter the number "))
        else:
            print("guess lower")
            incoming = int(input("enter the number "))


