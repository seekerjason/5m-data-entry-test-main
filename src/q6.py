def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    i=0
    lislen=len(lst)
    rtn="No negatives"
    while i<lislen:
        x=lst[i]
        if type(x)==int and x<0:
            rtn=f"The first negative number={x}"
            break
        i+=1

    return rtn


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

lst=[[3, 5, -1, 7, -2, 8],[2, 10, 7, 0]]
for x in lst:
    print(f"find_first_negative({x})  return={find_first_negative(x)}")