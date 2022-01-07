lists = ["tea", "coffee", "biscuit", "sugar", "cookies"]
onotherlist = lists
print(id(lists))
print(id(onotherlist))
lists += ["milk_kova"]
print(lists)
print(onotherlist)
print(id(lists))
print(id(onotherlist))
a = b = c = d = e = f = onotherlist
b.append("cream")
print(d)
print(a)
print(lists)