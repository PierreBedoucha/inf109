'''taken from: http://code.activestate.com/recipes/66472/
'''

from math import ceil

# find best range function available to version (2.7.x / 3.x.x)
try:
    _xrange = xrange
except NameError:
    _xrange = range

def frange(start, stop = None, step = 1):
    """frange generates a set of floating point values over the
    range [start, stop) with step size step

    frange([start,] stop [, step ])"""

    if stop is None:
        for x in _xrange(int(ceil(start))):
            yield x
    else:
        # create a generator expression for the index values
        indices = (i for i in _xrange(0, int((stop-start)/step)))
        # yield results
        for i in indices:
            yield start + step*i