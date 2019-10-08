# Here we can store functions that are useful across all algorithms.


# Calculates the class distribution of a 2D list of data. The distribution is stored in a dictionary that maps each
# class to the proportion of examples in 'data' that have that class.
def calculate_class_distribution(data, class_col):
    n = len(data)
    # This is our map of each class to its probability/proportion:
    probs = {}
    for obs in data:
        class_val = obs[class_col]
        # We either update the probabilities if the class was already present, or initialize the probability if not.
        # Note that we divide by n here in order to prevent having to do it in a future iteration of the probability
        # map.
        if class_val in probs:
            probs[class_val] += 1 / n
        else:
            probs[class_val] = 1 / n
    return probs