# -----------------------------
# Escape Sequences Characters in Python
# \b => Backspace
# \newline => New line
# \\ => Backsplash
# \' => Single quote
# \" => Double quote"
# \n => New Line
# \r => Carriage Return
# \t => Tab
# \xhh => Character with hex value hh
# ------------------------------

# backspace
print("hello\b world") # hell world

# escape new line + \
print("hi \
this is a test") # hi this is a test

# backslash
print("c:\\User\\Documents\\python") # User\Documents\python

# single quote
print("this is a quote:\'hello to the end of the world\'") # this is a quote:'hello to the end of the world'

# double quote
print("this is a quote:\"hello to the end of the world\"") # this is a quote:"hello to the end of the world"

# new line
print("hello dear,\ncongrats in the new achievment.") # hello dear,
# congrats in the new achievment.

# carriage return
print("12345\r678") # 67845

# tab
print("hello\tworld") # hello   world

# hex value
print("\x48\x65\x6c\x6c\x6f") # Hello