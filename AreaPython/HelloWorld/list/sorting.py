even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
even.extend(odd)
print(even)
another_even = even
print(another_even)
even.sort()
print(even)
print(another_even)

evens = [2, 4, 6, 8, 0, 22, 12]
odds = [1, 3, 5, 7, 9]
ev = sorted(evens)
print(ev)
print(evens)
letter = sorted("The quick brown fox jumps over the lazy dog")
print(letter)
in_case = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
                            # casefold paathu () varathu namma fuction na kuppadula anga enna pannanu nu the mention
                            # panro key la
print(in_case)

sorted = sorted("podu aatam podu")
print(sorted)

# python converts 0r bind built-in function also to the variable name
# Then it will act as variable name not function
# See below example


# letters = sorted("abcdefghijklmmnopqrstuvwxyz")
# print(letters)
