'''
Tests for the `Technology` class.
'''
from nose import with_setup
from circuits.technology import Technology
from circuits.variables import *


TECH1_NAME = 'FIRST'
TECH1_CIRCUIT = X[0] & X[1] & X[2]
TECH1_COST = 0
TECH2_NAME = 'SECOND'
TECH2_CIRCUIT = X[0] | X[1] | X[2]
TECH2_COST = 1


def test_creation():
    t1 = Technology(TECH1_NAME, TECH1_CIRCUIT, TECH1_COST)
    t2 = Technology(TECH2_NAME, TECH2_CIRCUIT, TECH2_COST)
    assert t1.name == TECH1_NAME
    assert t1.cost == TECH1_COST
    assert t2.name == TECH2_NAME
    assert t2.cost == TECH2_COST


def test_satisfies():
    t1 = Technology(TECH1_NAME, TECH1_CIRCUIT, TECH1_COST)
    t2 = Technology(TECH2_NAME, TECH2_CIRCUIT, TECH2_COST)
    pass
