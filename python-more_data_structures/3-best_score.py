def best_score(a_dictionary):
    # Initialize the best score and the corresponding key to None
    best_key = None
    best_score = None

    # Loop through the dictionary and update the best score and key if necessary
    for key, value in a_dictionary.items():
        if best_score is None or value > best_score:
            best_key = key
            best_score = value
    
    # Return the best key
    return best_key
