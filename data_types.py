# bool for boolean
# str for strings
# int for integers (whole numbers)
# float for floating point numbers (decimals)

# dynamic typing (determined at runtime)
x = 5.5 # defines a float
print(f"x is of type {type(x)}")

# variables can change type
x = "a string"
print(f"x is of type {type(x)}")

# python is strongly typed, but not statically typed (as is seen above)
# This will cause a runtime error
#x = 5.5 + "string"
#print(f"{x}")

# strings
forename = "Jon"
surname = "Alan"

# concat with strings
full_name = forename + surname
print(f"{forename} {surname} has the fullname {full_name} with length {len(full_name)}")

# numeric types
# mixed numeric type operations are supported, with the "narrower" type being widened to the other
x, y = 10.5, 3
z = x + y
print (f"{x} + {y} = {z} # z is a {type(z)}") 

# boolean

result = x < y
print(f"{x} < {y} = {result} which is of type {type(result)}")