name = 'logesh'
for ch in name:
    print(ch)

nn = "37:653:43'6/  \:63/22"
separator = ""
for ch in nn:
    if not ch.isnumeric():
        separator += ch
print(separator)
