def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct.keys(): 
        print(f"The original value = {dct[key]} for key={key}")
        dct[key]=value
    else:
        dct[key]=value    
    #the function could just return nothing as the dct has been modified 
    #however, to comply with the problem requirement, the following code explicitly return the modified dct
    
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

diclist=[
    {'dic':{}, 'key':"name", 'value':"Alice"},
    {'dic':{"age": 25}, 'key':"age", 'value':26}
]
for x in diclist:
    print(f"original dict={x['dic']}")
    dct=update_dictionary(x['dic'],x['key'], x['value'])
    #the following code also print the modified dictionary. 
    #print(f"modified dict={x['dic']}")

    #however, to comply with the problem requirement, here use the returned dictionary 
    print(f"modified dict={dct}")
