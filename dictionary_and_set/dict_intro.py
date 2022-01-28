vechicles = {
    'dream': 'honda 250',
    'roadster': 'bmw r1100',
    "er5": "kawasaki er5",
    "virago": "yamaha xt650"
}
my_car = vechicles["dream"]
print(my_car)
my = vechicles["virago"]  # INDEXING RETURNS KEY ERROR WHEN KEY IS WRONG (INDEXING IS FASTER THAN GET)
# BUT USE ONLY U KNOW KEY
print(my)
new = vechicles.get("ER5")  # .GET RETURNS NONE WHEN KEY IS WRONG (USE WHEN U  NOT  SURE IN  KEY IS CORRECT OR NOT)
print(new)
print()
print()

# Adding items
vechicles["star"] = "lockracer"
vechicles["toy"] = "glider"
for key in vechicles:
    print(key, vechicles[key], sep=" : ")
print("!111111111111111111111111111111")
vechicles["virago"] = "new yamaha"
for key, val in vechicles.items():  # MORE EFFICIENT
    print(key, val, sep=" : ")
del vechicles["virago"]
# del vechicles["f1"] ithu error key not present
result = vechicles.pop("f1",
                       "##########################podu illa")  # default aa error the varu pop la um ,ku apro namma pop
# kita sollula enna return aganu nu
print(result)
print("2222222222222222222222222222222222")
for key, val in vechicles.items():  # MORE EFFICIENT
    print(key, val, sep=" : ")

val = vechicles.pop("dream")
print("ithu present : ", val)
val = vechicles.pop("roadster", "not present")  # its is true actually
print(val)
