x, y = 8, 10 # assign multiple variables on a single line (pattern)
print("x is", x, "and y is", y)

# variable re-assignment
x, y = y, x # swap the values around
print("x is", x, "and y is", y)

module_code, module_Code = "case sensitive", "Case sensitive"
print("module_code is", module_code, "and module_Code is", module_Code)

# interpolation with fstring
print(f"module_code is {module_code}, but interpolated with fstring")                                                                           