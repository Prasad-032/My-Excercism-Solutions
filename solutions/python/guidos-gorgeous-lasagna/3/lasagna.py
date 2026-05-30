"""Functions used in preparing Guido's gorgeous lasagna."""
PREPARATION_TIME = 2    
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time): 
    """ Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """   
    return EXPECTED_BAKE_TIME - elapsed_bake_time  


def preparation_time_in_minutes(layers):
    """ Calculate the preparation time required for the layers.

    Parameters:
        layers (int): The number of layers

    Returns:
        int: the total preparation time in minutes for the number of layers

    Function that takes the actual number of layers and multiplied by the
    preparation time to calculate the total preparation time for all layers.
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """ Calculate the total elapsed cooking time.
    Parameters:
      layers(int): The number of layers,
      elapsed_bake_time: the time already taken to bake

    Returns:
        int: the total elapsed time in minutes

    Function that takes the actual number of layers and elapsed bake time as
    inputs and calculates the elapsed time in minutes by using preparation
    time in minutes function with the argument of layers and adds it to the
    elapsed bake time.    
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
