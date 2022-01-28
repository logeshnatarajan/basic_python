from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken : {chicken_quantity}")
beans_quantity = pantry.setdefault("beans", 0)  # default value la enna vennalu kudukala ex: string mari
print(f"beans : {beans_quantity}")
ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup : {ketchup_quantity}")
print()
print("pantry now contains ")
for key, item in sorted(pantry.items()):
    print(f"{key} : {item}")
# SETDEFAULT GET KU IRRUKARA DIFF ENNA NA SETDEFAULT LA KEY ILLANA DEFAULT VALUE AA RETURN PANNITU
# ANTHA KEY A CREATE PANNU GET DEFAULT VALUE VA MATTUM THA RETURN PANNU NEW KEY CREATE PANNATHU
