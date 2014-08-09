'''
bitstring
~~~~~~~~~

Utilities for dealing with bit strings.
'''


def increment(bs):
    '''
    Increments the given bit string.

    :param bs: a bit string (list of integers)
    '''
    c = 1
    obs = []
    for b in reversed(bs):
        if b == c:
            obs.append(0)
        else:
            obs.append(1)
            c = 0
    if c == 1:
        obs = obs + [1]
    return list(reversed(obs))


def bitrange(length):
    '''
    Produces all possible bit strings up to the given length.

    :param length: the maximum length bit string to produce
    '''
    bs = [0] * length
    while len(bs) == length:
        yield bs
        bs = increment(bs)
