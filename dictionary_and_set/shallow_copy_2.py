lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]
animals2 = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list
}

an = animals2.copy()
an["teddy"].append("toy")
print(animals2["teddy"])
print(an["teddy"])
teddy_list.append("nothing")
print(animals2["teddy"])
print(an["teddy"])


# THIS IS SHALLOW COPYING ANIMALS2 LA IRRUKARA MARI THA PYTHON LA SAVE AIRUKUM LIST IRRUTHA ATHODA REFERENCE THA AIRUKUM
# SO NEE `AN` KU COPY PANNUNA ANTHA REFERNCE THA COPY AGU SO ANTHA LIST LA ETHULA(YATHA PALCE AA IRRUTHALU) CHANGE
# PANNUNALU ELLAMA PAKAMU REFLECT AGU

# DOUGHT IRRUTHA 205 PARU
