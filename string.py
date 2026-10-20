# ---------------------------
# --Strings in Python--
# ---------------------------




# you can use single quotes or double quotes to create a string in python.
myStringOne = 'Hello World!' # single quotes
myStringTwo = "Hello world!!" # double quotes

print(myStringOne) # Hello World!
print(myStringTwo) # Hello world!!

# if you are using single quotes to create a string you can use double quotes inside the string and vice versa.

myStringThree = 'Hello "World!"' # single quotes with double quotes inside
myStringFour ="Hello 'World'" # double quotes with single quotes inside

print(myStringThree) # Hello "World"!
print(myStringFour) # Hello 'World'

# if you want to make multiple lines of a string or using double quotes and single quotes inside the string you can use the triple quotes """ or '''.
myStringFive = """hello 
"Dear" Friend,"""


myStringSix = '''hello \
'I'm' Ms
'Lujain\'''' 
# output: hello 'im' Ms
# 'Lujain'

print(myStringFive) # hello world
print(myStringSix) # hello I'm Lujain