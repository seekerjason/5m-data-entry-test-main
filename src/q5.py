def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if type(num)==int and type(divisor)==int:
        if num % divisor == 0:
            return True
    return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
lst=[[10, 2], [7, 3]]
for x in lst:
    flg=check_divisibility(x[0],x[1])
    print(f"function {x[0],x[1]} returns {flg}")