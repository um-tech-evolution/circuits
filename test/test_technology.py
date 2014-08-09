'''
Tests for the `Technology` class.
'''
import unittest
from pyeda.inter import farray
from circuits.technology import Technology
from circuits.variables import *
from circuits.primitives import *


TECH1_NAME = 'FIRST'
TECH1_CIRCUIT = farray([X[0] & X[1] & X[2]])
TECH1_COST = 0
TECH1_VARS = {X[0], X[1], X[2]}
TECH2_NAME = 'SECOND'
TECH2_CIRCUIT = farray([X[0] | X[1] | X[2]])
TECH2_COST = 1
TECH2_VARS = {X[0], X[1], X[2]}


class TestTechnology(unittest.TestCase):
    def setUp(self):
        self.t1 = Technology(TECH1_NAME, TECH1_CIRCUIT, TECH1_COST)
        self.t2 = Technology(TECH2_NAME, TECH2_CIRCUIT, TECH2_COST)

    def test_creation(self):
        self.assertEqual(self.t1.name, TECH1_NAME)
        self.assertEqual(self.t1.cost, TECH1_COST)
        self.assertEqual(self.t2.name, TECH2_NAME)
        self.assertEqual(self.t2.cost, TECH2_COST)

    def test_satisfies(self):
        self.assertTrue(self.t1.satisfies(self.t1))
        self.assertFalse(self.t1.satisfies(self.t2))

    def test_better_than(self):
        self.assertTrue(OR.better_than(NAND, AND))
        self.assertFalse(NAND.better_than(OR, AND))

    def test_distance_from(self):
        self.assertEqual(AND.distance_from(AND), 0)
        self.assertEqual(AND.distance_from(OR), 2)
        self.assertEqual(AND.distance_from(NAND), 4)
        self.assertEqual(NAND.distance_from(XOR), 1)

    def test_inputs(self):
        self.assertEqual(self.t1.inputs(), TECH1_VARS)
        self.assertEqual(self.t2.inputs(), TECH2_VARS)
        self.assertEqual(AND.inputs(), {X[0], X[1]})
