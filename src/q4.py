def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if type(s)==str:
        return True, s[::-1]

    return False, f"The input is not a String type {s}!"

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

slst=["Hello World","Python",1231]
for x in slst:
    flg, rstr=string_reverse(x)
    if flg==True:
        print(f"the reversed string = {rstr}")
    else:
        print(f"{rstr}")