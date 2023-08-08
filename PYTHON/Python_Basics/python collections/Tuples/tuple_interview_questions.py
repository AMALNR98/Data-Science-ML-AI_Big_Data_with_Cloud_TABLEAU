# How to replace value in tuple (but tuple is immutable)

tu = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# from this tuple replace 20 to 25
tu_list = list(tu)  # converting tuple to list
tu_list[1] = 25
tu = tuple(tu_list)  # converting list to tuple
print(tu)
