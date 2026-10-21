# ---------------------------
# ----concatenation in python----
# ---------------------------   
# concatenation is the process of joining two or more strings together. In Python 
# you can concatenate strings using the + operator or by using the join() method.


msg1 = "hello"
msg2 = "world"

print(msg1 + " " + msg2)

letters = "a\
b\
c"

numbers = "1\
2\
3"

msg3 =letters + " " + numbers
print(msg3) # abc 123

gate = 4
# print(msg1 + gate) TypeError: can only concatenate str (not "int") to str