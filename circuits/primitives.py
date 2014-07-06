'''
primitives.py
Primitive logic circuit technologies.
'''


from .technology import Technology
from .variables import X
from pyeda.boolalg.bdd import BDDONE, BDDZERO
from pyeda.inter import farray


class _Nand(Technology):
    def __init__(self):
        super(_Nand, self).__init__('NAND', farray([~(X[0] & X[1])]))


class _And(Technology):
    def __init__(self):
        super(_And, self).__init__('AND', farray([X[0] & X[1]]))


class _Or(Technology):
    def __init__(self):
        super(_Or, self).__init__('OR', farray([X[0] | X[1]]))


class _Xor(Technology):
    def __init__(self):
        super(_Xor, self).__init__('XOR', farray([X[0] ^ X[1]]))


class _One(Technology):
    def __init__(self):
        super(_One, self).__init__('ONE', farray([BDDONE]))


class _Zero(Technology):
    def __init__(self):
        super(_Zero, self).__init__('ZERO', farray([BDDZERO]))


NAND = _Nand()
AND = _And()
OR = _Or()
XOR = _Xor()
ONE = _One()
ZERO = _Zero()
