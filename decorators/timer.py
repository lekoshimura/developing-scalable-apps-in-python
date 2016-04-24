# timer.py

import time

# Decorator function that prints the time that a function takes to run.
def timedFunction(func):
    # The wrapper function will take whatever arguments the original does.
    def wrapper(*args, **kwargs):
        # Call the function we're decorating, recording its start and end time.
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()

        # Calculate and print the elapsed time of the decorated function.
        elapsed = end - start
        print "%s took %2.4f seconds to run." % (func.__name__, elapsed)

        # Return the decorated function's value.
        return value
    return wrapper
