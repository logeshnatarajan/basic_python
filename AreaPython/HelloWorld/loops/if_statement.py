name = input("enter tour name : ")
age = int(input("enter your age, {0} ".format(name)))
print(age)
if age > 18:
    print("you are eligible to vote ")
elif age == 18:
    print("you are barely accepted enjoy")
else:
    print("too young to vote come back after {} years".format(18-age))
