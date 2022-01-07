num = [3, 6, 336, 5, 6, 5354, 46]
print(min(num))
print(max(num))
print(len(num))
word = "mississippi"
print(len(word))
print(word.count("s"))
print(word.count("S"))
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
number = even + odd
print(number)
even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)
words = ["arjun",
         "Logesh",
         "naveen",
         "Sathish"
         ]
print(words)
words.sort(key=str.casefold)
