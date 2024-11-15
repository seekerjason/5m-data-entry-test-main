def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if type(x)==int and type(y)==int:
        x, y = y, x
        print(f"the swapped values (x={x},y={y}).")
    else: 
        return -1

    return 1


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

x=["Apple",9]
y=[10,17]
for z in range(2):
    if swap(x[z], y[z])==-1:
        print(f"Non-numeric value presented (x={x[z]},y={y[z]})! Return -1.")
