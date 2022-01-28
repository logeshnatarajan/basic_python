from simple_deepcopy import my_deepcopy
import copy

original = {
    "tim": ["buchalka", ["programmer", "Teacher"]],
    "j-p": ["robert", ["programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

print(original)
print(copy_1)
print(copy_2)

original["tim"].append("summa")
original["j-p"].append("vetti")
print(original)
print(copy_1)
print(copy_2)
# try this above value va tha copy panra fucn la so athukulla irrukara list reference tha airuku (value matum copy panra
# nalla full dict copy pannala nalla puruchukoo haha
original["tim"][1].append("cashier")
original["j-p"][1].append("motor")
print(original)
print(copy_1)
print(copy_2)
# DEEP COPY USES RECURSION SO WHEN IT ENCOUNTER MUTABLE IN MUTABLE LIKE ABOVE LIST IN LIST IT CALLS ITSELF AGAIN
