# //////////////////
# --- Variables ---
# [syntax] => variable_name = value

# Variable Name roles
# [1] Variable names can only start with a letter or an underscore (_)
# [2] variable can't start with a number or special character
# [3] Variable names can only contain letters, numbers, and underscores (no special characters such as @, $, and %)
# [4] Variable names are case-sensitive (age, Age, and AGE are three different variables)
# //////////////////

my_variable ="Hello, World!" # string variable
print(my_variable) # Hello, World!
print(type(my_variable)) # str => String



# variable naming Best Practices
name = "Lujain" # single word => Normal
firstName = "Lujain" # multi word => camelCase 
first_name = "Lujain" # multi word => snake_case

print(name) # Lujain
print(firstName) # Lujain
print(first_name) # Lujain