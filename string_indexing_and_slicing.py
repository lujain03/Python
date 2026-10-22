# -----------------------------
# String Indexing and Slicing
# [1] All Data in python is objects and strings are an object in python.
# [2] object contains elements and each element has an index.
# [3] Indexing is used to access individual elements in a string.
# [4] python uses zero-based indexing
# [5] use square brackets [] to access elements in a string.
# [6] Slicing is used to access a range of elements in a string.
# [7] Enable to access parts of strings, Tuples or lists
# ------------------------------

# indexing (Access single item)

myString = "I Love Python"
print(myString[0]) # Index 0 is I
print(myString[9]) # Index 9 is t

print(myString[-1]) # Index -1 is n
print(myString[-5]) # Index -5 is y


# slicing (Access a Multiple items)
# [start:End]
print(myString[2:6]) # Index 2 to 5 is Love bc the end is not included
print(myString[1:]) # Index 1 to end is Love Python
print(myString[:6]) # Index 0 to 5 is I Love
print(myString[-4:-1]) # tho

# print(myString[-1:4])  Index -1 to 4 is empty string bc the end is not included

# [start:End:Steps]
print(myString[0::1]) #full string
print(myString[::2]) #ILv yhn
print(myString[2:9:2]) #Lv y
print(myString[::-1]) # nohtyP evoL I