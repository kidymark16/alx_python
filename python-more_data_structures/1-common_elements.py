def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common = set()
    
    # Iterate over the elements in the first set
    for elem in set_1:
        # If the element is also in the second set, add it to the common set
        if elem in set_2:
            common.add(elem)
    
    return common
