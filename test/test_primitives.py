'''
Tets for technology primitives.
'''
from nose import with_setup
from circuits.primitives import *
from circuits.variables import *


def test_nand():
    assert evaluated_at(NAND.circuit, [1,1]) == [0]
    assert evaluated_at(NAND.circuit, [0,1]) == [1]
    assert evaluated_at(NAND.circuit, [1,0]) == [1]
    assert evaluated_at(NAND.circuit, [0,0]) == [1]


def test_and():
    assert evaluated_at(AND.circuit, [1,1]) == [1]
    assert evaluated_at(AND.circuit, [0,1]) == [0]
    assert evaluated_at(AND.circuit, [1,0]) == [0]
    assert evaluated_at(AND.circuit, [0,0]) == [0]


def test_or():
    assert evaluated_at(OR.circuit, [1,1]) == [1]
    assert evaluated_at(OR.circuit, [0,1]) == [1]
    assert evaluated_at(OR.circuit, [1,0]) == [1]
    assert evaluated_at(OR.circuit, [0,0]) == [0]


def test_xor():
    assert evaluated_at(XOR.circuit, [1,1]) == [0]
    assert evaluated_at(XOR.circuit, [0,1]) == [1]
    assert evaluated_at(XOR.circuit, [1,0]) == [1]
    assert evaluated_at(XOR.circuit, [0,0]) == [0]


def test_one():
    assert evaluated_at(ONE.circuit, [1]) == [1]
    assert evaluated_at(ONE.circuit, [0]) == [1]


def test_zero():
    assert evaluated_at(ZERO.circuit, [1]) == [0]
    assert evaluated_at(ZERO.circuit, [0]) == [0]
