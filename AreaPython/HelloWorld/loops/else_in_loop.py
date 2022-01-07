number = [1, 13, 34, 25, 31, 55, 66]
for i in number:
    if i % 8 == 0:
        print("not eligible")
        break
else:
    print("everything is fine")
# if for loop execute normally without breaking else block execute
