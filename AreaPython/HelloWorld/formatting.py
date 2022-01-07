for i in range(1, 13):
    print("no : {0} square is {1} cube is {2}".format(i, i ** 2, i ** 3))
# kela iruukaratbu replacement field nu peru
print()
for i in range(1, 13):
    print("no : {0:2} square is {1:3} cube is {2:4}".format(i, i ** 2, i ** 3))  # right align
print()
for i in range(1, 13):
    print("no : {0:2} square is {1:<3} cube is {2:<4}".format(i, i ** 2, i ** 3))  # left align

print()
for i in range(1, 13):
    print("no : {0:2} square is {1:^3} cube is {2:^4}".format(i, i ** 2, i ** 3))  # center align
print()
print("pi is approximately {0:12}".format(22 / 7))
print("pi is approximately {0:12f}".format(22 / 7))
print("pi is approximately {0:50.50f}".format(22 / 7))
print("pi is approximately {0:62.50f}".format(22 / 7))
print("pi is approximately {0:72.64f}".format(22 / 7))
# intha : vanthu evalo space vennu nu solrathu apro antha . vanthu decimal ponits ku apro evalo number nu kamika
print()
for i in range(1, 13):
    print("no : {} square is {} cube is {:^5}".format(i, i ** 2, i ** 3))
