
# ------------------
# --strings methods--
# ------------------


# [1] length len()
a = "i love python"
print(len(a))
print(a)

# [2] strip() rstrip() lstrip() 
# use strip to cut the white spaces even from left and right or just left or right 
b = "           i love myself       "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

c ="#####hello there####"
print(c.strip("#"))

# [3] title()  make all the first letters capital
d = "I love 2d Graphics and 3g Technology and python"
print(d.title())


# [4] capitalize() just the first word have the capita letter
e = "i love 2d Graphics and 3g Technology and python"
print(e.capitalize())

# [5] zfill --- I didnt like it :)


# [6] upper()
f = "oSama"
print(f.upper())
print(f.lower())