'''
exceptions.py
Exception classes for circuits implementation.
'''

class DimensionException(Exception):
    '''
    Raised when the dimensions (number of inputs, specifically) for the list of
    BDDs provided to a circuit are inconsistent.
    '''
    pass
