# decorated.py
#
# Try running this code as it is.
# Then decorate the sumUp function by uncommenting the decorator call on the
# line above it, and run it again.
#
# To see the source for the decorator, look in the "timer.py" tab.

import timer

# Decorate me!  Uncomment the next line.
@timer.timedFunction
def sumUp(n):
    total = 0
    for x in range(n):
        total += x
    return total

print sumUp(10000000)
