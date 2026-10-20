# ///////////////
# type()
# All data in python is an object, and every object has a type. The type() function returns the type of the object passed to it.
# //////////////

print(type(5)) #int => Integer
print(type(5.5)) #float => Floating point number


print (type("hello python")) #str => String

print(type([1,2,3])) #list => List

print(type((1,2,3))) #tuple => Tuple

print(type({1,2,3})) #set => Set

print(type({"name":"Lujain", "age":23})) #dict => Dictionary

print(type(2==2)) #bool => Boolean
print(type(True)) #bool => Boolean

# until now the types is str, int, float, list, tuple, set, dict, bool