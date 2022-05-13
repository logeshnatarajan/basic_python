# use of break statement
for i in range(20):
    if i == 8:
        print("done found num : {}".format(i))
        break
    print(i)

num = None  # its like a null or _ in golang
lists = [1, 2, 3, 4, 5]
print(lists[1])
print(lists[4])
for index in range(len(lists)):
    if index == 6:
        num = index
print("num : {}".format(num))
print()
num = 2
if num in lists:
    print(lists.index(num))
