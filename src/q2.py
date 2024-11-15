def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    flg=True
    if type(lst)==list:
        for x in range(len(lst)):
            if lst[x]==find_val:
                lst[x]=replace_val
    else:
        flg=False
        print(f"the input {lst} is not a list!")
    return flg, lst
    

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

olst=[
        {'lst':[1, 2, 3, 4, 2, 2], 'findval':2, 'replval':5}, 
        {'lst':["apple", "banana", "apple"],'findval':"apple", 'replval':"orange"},
        {'lst':123, "findval":1, "replval":2}
     ]
for x in olst:
    print(f"original list={x['lst']}")
    flg, lst=find_and_replace(x['lst'], x['findval'], x['replval'])
    #in fact, the x['lst'] at this point has been modified with the replace value. 
    #print(f"modified list={x['lst']}") will have the same result.
    #since it is required to return the modified list from the function, the following takes the return list instead.
    if flg==True:
        print(f"modified list={lst}")
