
PREPERATION_TIME = 2
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - int(elapsed_bake_time)

def preparation_time_in_minutes(number_of_layers):
    return int(number_of_layers) * PREPERATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return (int(number_of_layers) * PREPERATION_TIME) + int(elapsed_bake_time)

def total_time_in_minutes (number_of_layers, actual_bake_time):
    return (int(number_of_layers) * PREPERATION_TIME) + int(actual_bake_time)