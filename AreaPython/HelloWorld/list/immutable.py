# result = True
# no = result
# print(id(result))
# print(id(no))
# result = False
# print(id(result))

result = "yes"
no = result
print(id(result))
print(id(no))
result += "s"
print(id(result))
print(id(no))
