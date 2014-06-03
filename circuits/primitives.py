'''
primitives.py
Primitive logic circuit technologies.
'''


from .technology import Technology
from .variables import X
from pyeda.boolalg.bdd import BDDONE, BDDZERO


class _Nand(Technology):
    def __init__(self):
        super(Nand, self).__init__('NAND', [~(X[0] & X[1])])


class _And(Technology):
    def __init__(self):
        super(And, self).__init__('AND', [X[0] & X[1]])


class _Or(Technology):
    def __init__(self):
        super(Or, self).__init__('OR', [X[0] | X[1]])


class _Xor(Technology):
    def __init__(self):
        super(Xor, self).__init__('XOR', [X[0] ^ X[1]])


class _One(Technology):
    def __init__(self):
        super(One, self).__init__('ONE', [BDDONE])


class _Zero(Technology):
    def __init__(self):
        super(Zero, self).__init__('ZERO', [BDDZERO])


NAND = _Nand()
AND = _And()
OR = _Or()
XOR = _Xor()
ONE = _One()
ZERO = _Zero()
