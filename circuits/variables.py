'''
variables
~~~~~~~~~

Shared set of boolean variables for use in all technologies. Two special
constants are exported.

`X` is the vector of BDD variables that are available for use in all circuits.
These can be used, once imported, by indexing `X` like a list: ``X[0]``, etc.

`N` is the length of the `X` vector.
'''


from pyeda.inter import bddvars


# The number of total variables that will be allocated. Set to 16 based on the
# requirements found in [1] W. Arthur and W. Polak, “The evolution of
# technology within a simple computer model,” Complexity, vol. 11, no. 5, pp.
# 23–31, 2006.
N = 16


X = bddvars('x', N)


def evaluated_at(circuit, bitstring):
    '''
    Evaluates the given circuit (function array) at the given bitstring and
    returns the resulting bitstring. The input and output bitstrings will be
    lists of `0` and `1`. If the input bitstring is shorter than `N`, it will
    be padded to the right with zeroes.

    :param circuit: the boolean circuit to evaluate
    :param bitstring: a list of `0` and `1` integers
    '''
    if len(bitstring) < N:
        inbits = bitstring + [0] * (N - len(bitstring))
    else:
        inbits = bitstring

    return [int(e) for e in circuit.vrestrict({X: inbits})]
